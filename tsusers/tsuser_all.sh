WD=/root/bolt/tsusers
XRDPD=$WD/xrdp_servers
XRDPDLS=`ls $XRDPD`
ATL=$WD/tsadmins.lst


for i in ${XRDPDLS[@]}; do

  bolt file upload $XRDPD/${i}  /tmp/tsusers.lst  --targets ${i}
  bolt file upload $ATL /tmp/tsadmins.lst --targets ${i}
  bolt script run $WD/populate_tsusers_group.sh --targets ${i}

done
