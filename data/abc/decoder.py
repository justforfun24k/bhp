import base64
import os

files=os.listdir('.')

for file in files:
	if file != 'decoder.py':
		fd=open(file,'rb')
		lines=fd.readlines()
		for line in lines:
			data=base64.b64decode(line.strip())
			print data
		fd.close()

