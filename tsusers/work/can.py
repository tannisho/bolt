uft = '/bolt/tsusers/work/username_fullname_table'
mf = '/tmp/userlist_delimited.csv'
sn = {}
ufth = {}
ufthm = {}
fu = {}

with open(mf, 'r') as ff:
	for i in ff:
		i = i.strip()
		ac,fn,xs = i.split(',')
		if (fn != "" and fn != "Analyst Name" ):
		        fn = fn.split()[-1]
			striped = fn[0:5]
			sn[striped] = xs

with open(uft, 'r') as gg:
	for j in gg:
		j = j.strip()
		un2,fn2 = j.split(':')
		ufth[un2] = fn2

for k, v in ufth.items():
	vm = v.split()[-1]
	vm = vm[0:5]	
	for l in sn:
		if l == vm:
			fu[l] = 1
			ufthm[k] = sn[l]
#			print(v, k, sn[l])

for n in ufthm:
	print(n+':'+ufthm[n])
	
		
for m in sn:
	if not m in fu:
		print('NOT FOUND:'+m+':'+sn[m])

