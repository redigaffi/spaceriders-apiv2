#!/bin/bash

wallet=0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266
database_name=spaceriders_testnet
uri=mongodb://root:example@localhost:27017/

if [ "$1" == "-h" ]; then
    echo "Usage: $(basename "$0") [-d DATABASE] [-u URI] [-w WALLET]"
    echo "  -d DATABASE		Database name you want to use		(Default: $database_name)"
    echo "	-u URI			URI of the database					(Default: $uri)"
    echo "  -w WALLET       Account waller address              (Default: $wallet)"
    echo "	-h				Show help command"
    echo "	Show all planets owned by a given account."
    exit 0
fi

while getopts ":d:u:w:" option; do
    case "$option" in
    \?)
        echo "Invalid argument(s)."
        echo "Use -h to show help."
        exit 1
        ;;
    d)
        database_name=$OPTARG
        ;;
    u)
        uri=$OPTARG
        ;;
    w)
        wallet=$OPTARG
        ;;
    esac
done

mongosh "$uri" <<EOF
use $database_name
db.planets.find( { user: "$wallet" }, { _id: true, name: true, level: true, reserves: true, resources: true, resources_level: true, installation_level: true, research_level: true })
exit
EOF
