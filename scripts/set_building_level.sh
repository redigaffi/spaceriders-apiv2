#!/bin/bash

database_name=spaceriders_testnet
uri=mongodb://root:example@localhost:27017/
id=NULL
resources_level=0
installation_level=0
research_level=0
defense_items=0

if [ "$1" == "-h" ]; then
    echo "Usage: $(basename "$0") [-d DATABASE] [-u URI] [-i ID] [-r RESOURCE] [-t INSTALLATION] [-s RESEARCH] [-f DEFENSE]"
    echo "      -d  DATABASE        Database name you want to use       (Default: $database_name)"
    echo "      -u  URI             URI of the database                 (Default: $uri)"
    echo "      -i  ID              ID of the planet                    (Default: $id)"
    echo "      -r  RESOURCE        Level for resources                 (Default: $resources_level)"
    echo "      -t  INSTALLATION    Level for installations             (Default: $installation_level)"
    echo "      -s  RESEARCH        Level for research                  (Default: $research_level)"
    echo "      -f  DEFENSE         Items for defense                   (Default: $defense_items)"
    echo "      -h                  Show help command"
    echo "      Set level for buildings of a given planet."
    exit 0
fi

while getopts ":d:u:i:r:t:s:f:" option; do
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
    r)
        resources_level=$OPTARG
        ;;
    t)
        installation_level=$OPTARG
        ;;
    s)
        research_level=$OPTARG
        ;;
    f)
        defense_items=$OPTARG
        ;;

    esac
done

mongosh "$uri" <<EOF
use $database_name
db.planets.findAndModify( {
query: { _id : ObjectId("$id") },
update: { \$set: { 'resources_level.\$[].current_level': $resources_level,
                   'installation_level.\$[].current_level': $installation_level,
                   'research_level.\$[].current_level': $research_level,
                   'defense_items.\$[].quantity': $defense_items } },
} )
exit
EOF
echo ""
