#!/bin/sh

set -e

VERSION=2.71
NAME="blender-2.71-linux-glibc211-x86_64"
CACHE="${HOME}/.blender-cache"
TAR="${CACHE}/${NAME}.tar.bz2"
URL="http://mirror.cs.umn.edu/blender.org/release/Blender2.71/blender-2.71-linux-glibc211-x86_64.tar.bz2"

echo "Installing Blender ${VERSION}"
mkdir -p $CACHE
if [ ! -f $TAR ]; then
    wget -O $TAR $URL
fi
tar -xjf $TAR -C $HOME

echo "export BLENDER_BIN=\"${HOME}/${NAME}/blender\"" > .envs
