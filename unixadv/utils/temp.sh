#!/bin/bash
set -o nounset
set -o errexit
mydir=$(dirname $(readlink -f $0))/..
tempdir=$(mktemp -d)
cp -r $mydir $tempdir
echo $tempdir
