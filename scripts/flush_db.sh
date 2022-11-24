#!/bin/bash

database_name=spaceriders_testnet
uri=mongodb://root:example@localhost:27017/

if [ "$1" == "-h" ]; then
	echo "Usage: $(basename "$0") [-d DATABASE] [-u URI]"
	echo "	-d DATABASE		Database name you want to use		(Default: $database_name)"
	echo "	-u URI			URI of the database					(Default: $uri)"
	echo "	-h				Show help command"
	echo "	Drop all collections inside DB."
	exit 0
fi

while getopts ":d:u:" option; do
	case "$option" in
	\?)
		echo "Invalid argument(s)."
		echo "Use -h to show help."
		exit 1
		;;
	d)
		database_name=$OPTARG
		;;
	u) uri=$OPTARG ;;
	esac
done

mongosh "$uri" <<EOF
use $database_name
db.dropDatabase()
exit
EOF
echo ""
