BUILD = ./dist
PKG_RELEASE_NAME = i3-balance-workspace
PKG_LOCAL_NAME = i3_balance_workspace

.PHONY: build
build:
	poetry build

.PHONY: install
install: build
	current_version="$$(grep -r version pyproject.toml | sed -re 's/.*"([0-9.]*)"/\1/g')"; \
	pip install "$(BUILD)/$(PKG_LOCAL_NAME)-$$current_version-py3-none-any.whl"

.PHONY: uninstall
uninstall:
	pip uninstall $(PKG_RELEASE_NAME)

.PHONY: release.major
release.major: VERSION=$(shell poetry version major &> /dev/null; grep -r version pyproject.toml | sed -re 's/.*"([0-9.]*)"/\1/g')
release.major: release

.PHONY: release.minor
release.minor: VERSION=$(shell poetry version minor &> /dev/null; grep -r version pyproject.toml | sed -re 's/.*"([0-9.]*)"/\1/g')
release.minor: release

.PHONY: release.patch
release.patch: VERSION=$(shell poetry version patch &> /dev/null; grep -r version pyproject.toml | sed -re 's/.*"([0-9.]*)"/\1/g')
release.patch: release

.PHONY: release
release:
	version=$(VERSION); \
	if [ -z $$version ]; then \
		exit 1; \
	else \
		git checkout master; \
		sed -i -re "s/pkgver=([0-9.]*)/pkgver=$$version/g" PKGBUILD; \
		git add pyproject.toml; \
		git add PKGBUILD; \
		git commit -m "Release v$$version"; \
		poetry publish --build; \
		git tag -m v$$version v$$version; \
		git push --follow-tags; \
		sleep 300; \
		aur-release "$(PKG_RELEASE_NAME)" "$$version"; \
	fi;
