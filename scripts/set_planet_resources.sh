#!/bin/bash

database_name=spaceriders_testnet
uri=mongodb://root:example@localhost:27017/
id=NULL
metal=5000
crystal=5000
petrol=5000
energy=5000
bkm=5000

if [ "$1" == "-h" ]; then
    echo "Usage: $(basename "$0") [-d DATABASE] [-u URI] [-i ID] [-m METAL] [-c CRYSTAL] [-p PETROL] [-e ENERGY] [-b BKM]"
    echo "      -d  DATABASE    Database name you want to use       (Default: $database_name)"
    echo "      -u  URI         URI of the database                 (Default: $uri)"
    echo "      -i  ID          ID of the planet                    (Default: $id)"
    echo "      -m  METAL       Quantity of metal                   (Default: $metal)"
    echo "      -c  CRYSTAL     Quantity of crystal                 (Default: $crystal)"
    echo "      -p  PETROL      Quantity of petrol                  (Default: $petrol)"
    echo "      -e  ENERGY      Quantity of energy                  (Default: $energy)"
    echo "      -b  BKM         Quantity of BKM                     (Default: $bkm)"
    echo "      -h              Show help command"
    echo "      Set resources for a given planet."
    exit 0
fi

while getopts ":d:u:i:m:c:p:e:b:" option; do
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
    e)
        energy=$OPTARG
        ;;
    b)
        bkm=$OPTARG
        ;;
    esac
done

mongosh "$uri" <<EOF
use $database_name
db.planets.findAndModify( {
query: { _id: ObjectId("$id") },
update: { \$set: { resources: { metal: $metal, crystal: $crystal, petrol: $petrol, energy: $energy, bkm: $bkm } } },
} )
exit
EOF
echo ""
