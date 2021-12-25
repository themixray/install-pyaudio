import struct
import shutil
import sys
import os

st = str(8*struct.calcsize("P"))
v = list(sys.version_info[:3])

path = os.path.abspath(f'x{st}')
whl = ''
for i in os.listdir(path):
	wx = i.split('.')[:-2]
	wi = 0
	for n in range(len(wx)):
		if int(wx[n]) == v[n]:
			wi += 1
		if wi > len(wx)-1:
			whl = os.path.join(path,i)
	if whl != '':
		break
nn = f'PyAudio-0.2.11-cp{"".join(wx)}-cp{"".join(wx)}{"m" if int(wx[0]) < 3 or int(wx[1]) < 8 else ""}-win{"_amd64" if st == "64" else "32"}.whl'
shutil.copy(whl,os.path.join(os.path.abspath('.'),nn))
os.system(f'pip install "{nn}"')