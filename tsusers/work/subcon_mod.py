import re
import pwd
mf = 'list.csv'

with open(mf, 'r') as ff:
        for i in ff:
                i = i.strip()
                f,s,t = i.split(',')
#		if re.findall(r"^[0-9]{5}$", s):
                t = re.sub(r"^SRATS_xRDP_01", "10.40.1.41", t)
                t = re.sub(r"^SRATS_xRDP_02", "10.40.1.42", t)
                t = re.sub(r"^SRATS_xRDP_03", "10.40.1.43", t)
                t = re.sub(r"^SRATS_xRDP_04", "10.40.1.44", t)
                t = re.sub(r"^SRATS_xRDP_05", "10.40.1.45", t)
                t = re.sub(r"^SRATS_xRDP_06", "10.40.1.46", t)
                t = re.sub(r"^SRATS_xRDP_07", "10.40.1.47", t)
                t = re.sub(r"^SRATS_xRDP_08", "10.40.1.48", t)
                print(s+":"+t)
