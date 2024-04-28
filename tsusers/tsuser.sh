WD=/bolt/tsusers
XRDPS=`basename $1`
TL=$WD/xrdp_servers/$XRDPS
ATL=$WD/tsadmins.lst

if [ -z $1 ] ; then
        echo "Usage: $0 <tsusers_list>"
        echo "tusers lists are located in $TL"
        exit;
fi

bolt file upload $ATL /tmp/tsadmins.lst --targets $XRDPS
bolt script run $WD/populate_tsusers_group.sh --targets $XRDPS
