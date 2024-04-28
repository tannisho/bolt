DL=/tmp/1
XRDPD=../xrdp_servers
#XRDPD=/home/foobar1/bolt/tsusers/xrdp_servers

cd $XRDPD
awk -F":" '{print $1 > $2}' $DL
