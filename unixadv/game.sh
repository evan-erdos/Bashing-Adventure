#!/bin/bash
set -o nounset
set -o errexit
mydir=$(dirname $0)

if [ $# -lt 1 ];
then
    echo "Pass a subcommand";
    exit 0;
fi

subcmd=$1
shift;

if test -e $mydir/location/command/$subcmd;
then
    $mydir/location/command/$subcmd $*;
else
    $mydir/command/$subcmd $*;
fi
