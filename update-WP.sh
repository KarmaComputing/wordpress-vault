#!/bin/bash

set -x
set -e

DIRECTORY=$1
UPLOADS=$1/wp-content/uploads
BK_DIRECTORY=$DIRECTORY".bk"
USER=$2
SQL=$BK_DIRECTORY/$USER-$(date +"%d-%m-%Y")

# To unlock the files recursively
sudo chattr -R -i $DIRECTORY

#GO TO THE WORDPRESS DIRECTORY
cd $DIRECTORY

#BACKUP THE FOLDER
sudo -u $USER cp -r $DIRECTORY $BK_DIRECTORY

# backup DB
sudo -u $USER -- wp --path=$DIRECTORY db export $SQL

# update wordpress
sudo -u $USER -- wp core update 

# UPDATE PLUGIN
sudo -u $USER -- wp plugin update --all

#update themes
sudo -u $USER -- wp theme update --all

#Lock Script
sudo chattr -R +i $DIRECTORY && sudo chattr -R -i $UPLOADS && echo "Updates are now finished, all files are locked"
