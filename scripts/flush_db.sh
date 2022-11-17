#!/bin/bash

database_name=spaceriders_testnet
user=root
password=example
address=localhost
port=27017

if [ "$1" == "-h" ]; then
  echo "Usage: $(basename "$0") [-d DATABASE] [-u USER] [-c PASSWORD] [-a ADDRESS] [-p PORT]"
  echo "	-d DATABASE	Database name you want to use		(Default: $database_name)"
  echo "	-u USER		User you want to login with		(Default: $user)"
  echo "	-c PASSWORD	Password you use to login with		(Default: $password)"
  echo "	-a ADDRESS	Internet address of the server		(Default: $address)"
  echo "	-p PORT		Port the server is listening on		(Default: $port)"
  echo "	-h		Show help command"
  echo "Drop all collections inside DB."
  exit 0
fi

while getopts ":d:u:c:a:p:" option; do
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
    user=$OPTARG
    ;;
  c)
    password=$OPTARG
    ;;
  a)
    address=$OPTARG
    ;;
  p) port=$OPTARG ;;
  esac
done

mongosh "mongodb://$user:$password@$address:$port/" <<EOF
use $database_name
db.dropDatabase()
exit
EOF
echo ""
