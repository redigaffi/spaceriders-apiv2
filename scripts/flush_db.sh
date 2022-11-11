#!/bin/bash

database_name=spaceriders_testnet

if [ $# -eq 1 ]
then
	if [ "$1" == "-h" ] || [ "$1" == "--help" ]
	then
		echo "Usage: flush_db [DB] (spaceriders_testnet by default)."
		echo "Drop all collections inside DB."
		exit 0
	else
		database_name=$1
	fi

elif [ $# -gt 1 ]
then
	echo "Invalid option. Just one parameter allowed."
	exit 1
fi

docker-compose exec -T db mongosh "mongodb://root:example@localhost:27017/" <<EOF
use $database_name
db.dropDatabase()
show collections
exit
EOF
echo ""