import os


def ran(self):
	print "[*] In dirlister module"
	files=os.listdir(".")

	return str(files)
