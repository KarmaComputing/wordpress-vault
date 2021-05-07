#!/bin/bash

set -x 

DIRECTORY=/home/r2global/www/r2-commerce.com
UPLOADS=/home/r2global/www/r2-commerce.com/wp-content/uploads

# To unlock the files recursively
chattr -R -i $DIRECTORY

#wait for 30min in the background
(sleep 30m && chattr -R +i $DIRECTORY && chattr -R -i $UPLOADS && echo "Time as passed, all files are locked")&


