BUILD = ./dist
PKG_RELEASE_NAME = i3-balance-workspace
PKG_LOCAL_NAME = $(shell tr "-" "_" <<< $(PKG_RELEASE_NAME))
AUR_RELEASE_OPTIONS ?=

.PHONY: init
init:
	cp "./hooks/pre-commit" "./.git/hooks/"

.PHONY: build
build:
	poetry build

.PHONY: install
install: build
	pip install "$(BUILD)/$(PKG_LOCAL_NAME)-$(shell poetry version -s)-py3-none-any.whl"

.PHONY: uninstall
uninstall:
	pip uninstall --yes "$(PKG_RELEASE_NAME)"

.PHONY: release.major
release.major: VERSION = $(shell poetry version major &> /dev/null; poetry version -s)
release.major: release

.PHONY: release.minor
release.minor: VERSION = $(shell poetry version minor &> /dev/null; poetry version -s)
release.minor: release

.PHONY: release.patch
release.patch: VERSION = $(shell poetry version patch &> /dev/null; poetry version -s)
release.patch: release

.PHONY: release
release:
	version="$(VERSION)"; \
	if [ -z "$$version" ]; then \
		exit 1; \
	else \
		git checkout main; \
		git add pyproject.toml; \
		git commit -m "Release v$$version"; \
		git tag -m "v$$version" "v$$version"; \
		git push --follow-tags; \
		read -p "PyPi Username: " username; \
		read -p "PyPi Password: " password; \
		poetry publish --build --username "$$username" --password "$$password"; \
		sleep 300; \
		aur-release $(AUR_RELEASE_OPTIONS) "$(PKG_RELEASE_NAME)" "$$version"; \
	fi;
