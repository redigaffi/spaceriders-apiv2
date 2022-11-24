#!/bin/bash

database_name=spaceriders_testnet
uri=mongodb://root:example@localhost:27017/
id=NULL
metal_mine_health=0
crystal_mine_health=0
petrol_mine_health=0
metal_warehouse_health=0
crystal_warehouse_health=0
petrol_warehouse_health=0

if [ "$1" == "-h" ]; then
    echo "Usage: $(basename "$0") [-d DATABASE] [-u URI] [-i ID] [-m METAL_MINE] [-c CRYSTAL_MINE] [-p PETROL_MINE] [-x METAL_WAREHOUSE] [-y CRYSTAL_WAREHOUSE] [-z PETROL_WAREHOUSE]"
    echo "      -d  DATABASE            Database name you want to use       (Default: $database_name)"
    echo "      -u  URI                 URI of the database                 (Default: $uri)"
    echo "      -i  ID                  ID of the planet                    (Default: $id)"
    echo "      -m  METAL_MINE          Metal mine health                   (Default: $metal_mine_health)"
    echo "      -c  CRYSTAL_MINE        Crystal mine health                 (Default: $crystal_mine_health)"
    echo "      -p  PETROL_MINE         Petrol mine health                  (Default: $petrol_mine_health)"
    echo "      -x  METAL_WAREHOUSE     Metal warehouse health              (Default: $metal_warehouse_health)"
    echo "      -y  CRYSTAL_WAREHOUSE   Crystal warehouse health            (Default: $crystal_warehouse_health)"
    echo "      -z  PETROL_WAREHOUSE    Petrol warehouse health             (Default: $petrol_warehouse_health)"
    echo "      -h                      Show help command"
    echo "      Set health of buildings for a given planet."
    exit 0
fi

while getopts ":d:u:i:m:c:p:x:y:z:" option; do
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
        metal_mine_health=$OPTARG
        ;;
    c)
        crystal_mine_health=$OPTARG
        ;;
    p)
        petrol_mine_health=$OPTARG
        ;;
    x)
        metal_warehouse_health=$OPTARG
        ;;
    y)
        crystal_warehouse_health=$OPTARG
        ;;
    z)
        petrol_warehouse_health=$OPTARG
        ;;

    esac
done

mongosh "$uri" <<EOF
use $database_name
db.planets.findAndModify( {
query: { _id : ObjectId("$id") },
update: { \$set: { 'resources_level.0.health': $metal_mine_health,
                   'resources_level.1.health': $crystal_mine_health,
                   'resources_level.2.health': $petrol_mine_health,
                   'resources_level.3.health': $metal_warehouse_health,
                   'resources_level.4.health': $crystal_warehouse_health,
                   'resources_level.5.health': $petrol_warehouse_health, } },
} )
exit
EOF
echo ""
