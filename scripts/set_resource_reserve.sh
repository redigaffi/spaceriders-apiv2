#!/bin/bash

database_name=spaceriders_testnet
uri=mongodb://root:example@localhost:27017/
id=NULL
metal=1000000
crystal=1000000
petrol=1000000

if [ "$1" == "-h" ]; then
    echo "Usage: $(basename "$0") [-d DATABASE] [-u URI] [-i ID] [-m METAL] [-c CRYSTAL] [-p PETROL]"
    echo "      -d  DATABASE    Database name you want to use       (Default: $database_name)"
    echo "      -u  URI         URI of the database                 (Default: $uri)"
    echo "      -i  ID          ID of the planet                    (Default: $id)"
    echo "      -m  METAL       Quantity of metal reserves          (Default: $metal)"
    echo "      -c  CRYSTAL     Quantity of crystal reserves        (Default: $crystal)"
    echo "      -p  PETROL      Quantity of petrol reserves         (Default: $petrol)"
    echo "      -h              Show help command"
    echo "      Set resources reserves for a given planet."
    exit 0
fi

while getopts ":d:u:i:m:c:p:" option; do
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
    i)
        id=$OPTARG
        ;;
    m)
        metal=$OPTARG
        ;;
    c)
        crystal=$OPTARG
        ;;
    p)
        petrol=$OPTARG
        ;;
    esac
done

mongosh "$uri" <<EOF
use $database_name
db.planets.findAndModify( {
query: { _id : ObjectId("$id") },
update: { \$set: { reserves : { total_metal : $metal, total_crystal : $crystal, total_petrol : $petrol } } },
} )
exit
EOF
echo ""
