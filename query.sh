#!/bin/sh
Host=116.62.161.121
User=root
PW=123321
MSG=`mysql -h$Host -u$User -p$PW <<eof< font="">
show master status;
exit
EOF`
LOG=`echo $MSG |awk '{print $5}'`
mysql -h$Host -u$User -p$PW << FOE
purge master logs to “$LOG”;
exit
FOE
