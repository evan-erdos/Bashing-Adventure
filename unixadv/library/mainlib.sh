# NOTE: This is a library, intended for sourcing, not being executed.
set -o nounset
set -o errexit
room=$GAMEDIR/location
inventory=$GAMEDIR/inventory

function relpath(){
    python2 -c "import os.path; print os.path.relpath('$1','$GAMEDIR')"
}

function drop() {
    item=$1
    if test -e $inventory/$item;
    then
	mkdir -p $room/item/
	mv $inventory/$item $room/item/;
    else
	false
    fi
}

function get() {
    item=$1
    if test -e $room/item/$item;
    then
	mkdir -p $inventory
	mv $room/item/$item $inventory
    else
	false
    fi
}

function use_fixture() {
    fixture=$1
    shift
    if test -e $inventory/fixture/$fixture/use;
    then $inventory/fixture/$fixture/use $*
    else false
    fi
}

function use_item() {
    item=$1
    shift
    if test -e $inventory/$item/use;
    then $inventory/$item/use $*
    else false
    fi
}

function change_room() {
    link=$1
    if test -e $link;
    then
	dest=$(relpath $(readlink -f $link))
	ln -sfn $dest $GAMEDIR/location
    else
	false
    fi
}

function describe_room() {
    echo
    cat $room/name
    cat $room/name | tr '[a-zA-Z ]' '-'
    cat $room/description | fmt
}

function brief_describe_things() {
    things=$1
    if test -e $things;
    then
	ls $things | while read file;
	do cat $things/$file/brief_description;
	done
    fi
}

# prints the description of its argument, if it exists
function describe() {
    thing=$1
    if test -e $1;
    then
       cat $1/description | fmt;
    else
	false
    fi
}
