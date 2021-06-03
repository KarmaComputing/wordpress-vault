#!/bin/bash

set -x
set -e

DIRECTORY=$1
UPLOADS=$1/wp-content/uploads
BK_DIRECTORY=$DIRECTORY".bk"
USER=$2

# login as the user 
#sudo su $USER 

# To unlock the files recursively
sudo chattr -R -i $DIRECTORY

#GO TO THE WORDPRESS DIRECTORY
cd $DIRECTORY

# backup DB
sudo -u $USER -- wp --path=$DIRECTORY db export

#BACKUP THE FOLDER
sudo -u $USER cp -r $DIRECTORY $BK_DIRECTORY

# Delete database bk from production
sudo -u $USER rm -r $USER* 


# update wordpress
sudo -u $USER -- wp core update 

# UPDATE PLUGIN
sudo -u $USER -- wp plugin update --all

#update themes
sudo -u $USER -- wp theme update --all

#Lock Script
sudo chattr -R +i $DIRECTORY && sudo chattr -R -i $UPLOADS && echo "Updates are now finished, all files are locked"
