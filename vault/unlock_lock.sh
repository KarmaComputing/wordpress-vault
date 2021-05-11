#!/bin/bash

set -x 

DIRECTORY=$1
UPLOADS=$1/wp-content/uploads

# To unlock the files recursively
sudo chattr -R -i $DIRECTORY

#wait for 30min in the background
(sleep 30m && sudo chattr -R +i $DIRECTORY && sudo chattr -R -i $UPLOADS && echo "Time as passed, all files are locked")&


