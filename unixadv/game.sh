#!/bin/bash
export GAMEDIR=$(dirname $0)

if test $# -lt 1;
then
    echo "Pass a subcommand.";
    echo "Possible subcommands are:";
    ls $GAMEDIR/command
    exit 0;
fi

if [[ $1 = -s ]];
then
    # interactive mode
    exec xargs -n 1 -d '\n' -I % sh -c "$0 %"
fi

subcmd=$1
shift

if test -e $GAMEDIR/location/command/$subcmd;
then
    # run per-location command if it exists
    $GAMEDIR/location/command/$subcmd $*;
else
    # run default command otherwise
    $GAMEDIR/command/$subcmd $*;
fi
