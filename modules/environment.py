import os

class environment(object):
	def ran(self):
		print "[*] In environment module."
		return str(os.environ)
