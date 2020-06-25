SHELL = /bin/bash
BUILD = ./dist
GIT_HOOKS = ./.git/hooks

$(GIT_HOOKS)/pre-commit: ./hooks/pre-commit.sample
	cp --force $< $@

.PHONY: pre_commit_hook
pre_commit_hook: $(GIT_HOOKS)/pre-commit

.PHONY: build
build:
	poetry build

.PHONY: install
install: build
	version="$$(grep -r version pyproject.toml | sed -re 's/.*"([0-9.]*)"/\1/g')"; \
	pip install "$(BUILD)/i3_balance_workspace-$$version-py3-none-any.whl"

.PHONY: uninstall
uninstall:
	pip uninstall i3-balance-workspace

# install, uninstall, build, release with variants etc.
