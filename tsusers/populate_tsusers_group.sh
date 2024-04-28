#!/bin/bash
AUL=`cat /tmp/tsadmins.lst`

getent group tsusers 2> /dev/null

if [ $? -ne 0 ]
then
  groupadd tsusers
fi

gpasswd tsusers -M ''

for i in ${AUL[@]}; do

  usermod -a -G tsusers "${i}"

done
