import re
ml = '/tmp/2'
cd = {}

with open(ml, 'r') as ff:
	for i in ff:	
		i = i.strip()
		if re.search("^(?!UID).*", i):
			u,s = i.split(':')
			cd[u] = s

for j in cd:
	print(j+":"+cd[j])
