import random
list = '/tmp/1'
rn = ''

with open(list, 'r') as ff:
  for i in ff:
    i = i.strip()
    rn = random.randrange(1,9)
    print(i+','+'SRATS_xRDP_0'+str(rn))
