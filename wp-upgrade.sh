#!/bin/bash

set -x
set -e

DIRECTORY=$1
UPLOADS=$1/wp-content/uploads

# To unlock the files recursively
sudo chattr -R -i $DIRECTORY

#BACKUP THE FOLDER
cp -r $DIRECTORY $DIRECTORY".bk-$(date +"%d-%m-%Y")"

#GO TO THE WORDPRESS DIRECTORY
cd $DIRECTORY

# update wordpress
./wp-cli.phar core update --allow-root

# UPDATE PLUGIN
./wp-cli.phar plugin update --all --allow-root

#update themes
./wp-cli.phar theme update --all --allow-root

#Lock Script
sudo chattr -R +i $DIRECTORY && sudo chattr -R -i $UPLOADS && echo "Updates are now finished, all files are locked"
