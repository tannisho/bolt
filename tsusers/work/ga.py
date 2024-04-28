import os
import pwd
from collections import OrderedDict
xd='../tsusers/xrdp_servers'
rmdup = {}

xrdp_server_lists = os.listdir(xd)

for f in xrdp_server_lists:
	xdsf = (xd+'/'+f)
	with open(xdsf, 'r') as ff:
   		for i in ff:
			j = i.strip()
                        pw = pwd.getpwnam(j)
                        pwn = pw.pw_name
                        pwfn = pw.pw_gecos
  			#rmdup[pwn] = f
			print(pwn+':'+f)

#rmdupsorted = OrderedDict(sorted(rmdup.items()))
#for m in rmdupsorted:
#	print(m+':'+rmdupsorted[m])
