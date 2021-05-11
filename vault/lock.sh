#!/bin/bash

set -x 

DIRECTORY=/home/r2global/www/r2-commerce.com
UPLOADS=/home/r2global/www/r2-commerce.com/wp-content/uploads


sudo chattr -R +i $DIRECTORY && sudo chattr -R -i $UPLOADS 

if [[ $? -ne 0 ]]
then
   echo "Directory already locked"
else
   echo "All Files are locked"
fi

