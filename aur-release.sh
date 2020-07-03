#!/bin/sh
# Source: https://github.com/pbrisbin/aur-release/blob/master/bin/aur-release
# Used separately in order to modify the definition of mksrcinfo
# as well as adjustments to argument shifting
# The MIT License (MIT)
# Copyright (c) 2017 Pat Brisbin <pbrisbin@gmail.com>

set -e

if [ -z "$1" -o "$1" = "-h" -o "$1" = "--help" ]; then
  cat >&2 <<EOM
Usage: aur-release VERSION [NAME] [FILE, ...]
Tag and release an AUR package.
  VERSION       Version to release as; can be v1.2.3 or 1.2.3, the released
                package will always drop any leading "v" and the created git
                tags will always add it.
  NAME          Name of the package, defaults to the basename of the current
                working directory.
  FILE, ...     Files to copy into the AUR repository before releasing. This is
                most useful for an initial release. In such a case, don't forget
                to include the PKGBUILD itself. Files must be specified as
                relative to the project.
EOM
  exit 64
fi

version=$(echo "$1" | sed 's/^v//')
name=${2:-$(basename "$PWD")}
shift; shift
src_repo=$PWD
tmp_repo=$(mktemp -d)/$name

printf "Releasing %s as %s-%s...\n" "$src_repo" "$name" "$version"

git clone "ssh://aur@aur.archlinux.org/$name" "$tmp_repo"

(
  cd "$tmp_repo"

  for file; do
    cp -v "$src_repo/$file" .
    git add "$file"
  done

  updpkgsums
  makepkg --printsrcinfo > .SRCINFO

  git add .SRCINFO PKGBUILD
  git commit -m "Release v$version"
  git push
)

rm -rf "$tmp_repo"
