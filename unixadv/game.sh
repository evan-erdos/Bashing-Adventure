#!/bin/bash
mydir=$(dirname $0)

echo $#
if [ $# -lt 1 ];
then
    echo "Pass a subcommand";
    exit 0;
fi

subcmd=$1
shift;
$mydir/location/command/$subcmd $*
