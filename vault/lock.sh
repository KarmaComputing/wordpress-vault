#!/bin/bash

set -x 

DIRECTORY=$1
UPLOADS=$1/wp-content/uploads


sudo chattr -R +i $DIRECTORY && sudo chattr -R -i $UPLOADS 

if [[ $? -ne 0 ]]
then
   echo "Directory already locked"
else
   echo "All Files are locked"
fi

