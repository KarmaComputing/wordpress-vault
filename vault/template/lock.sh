#!/bin/bash

set -x 

DIRECTORY=/home/r2global/www/r2-commerce.com
UPLOADS=/home/r2global/www/r2-commerce.com/wp-content/uploads

#lock the Directory and Unlock the UPLOADS folder
chattr -R +i $DIRECTORY && chattr -R -i $UPLOADS && echo "Time as passed, all files are locked")&

