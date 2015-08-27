#! /usr/bin/python

import sys
class config():
	"""
good day today,nice weather,I mean
	"""	
	def __init__(self,file):
		self.conf=self.resolve_config(file)
			
	def resolve_config(self,file):
		ret=dict()
		with open(file) as f:
			for line in f:
				line=line.strip(" ")
				line=line.strip("\n")
				line=line.strip("\r")
				if line=="" or line[0]=='#':
					continue
				idx=line.find("=")
				if idx == -1:
					continue
				key=line[:idx].strip()
				val=line[idx+1:].strip()
				ret[key]=val
		return ret
	def key_exist(self,key):
		return key in self.conf
	def get_value(self,key):
		try:
			return self.conf[key]
		except:
			return None
	def dump_conf(self):
		for item in self.conf:
			print "%s --> %s"%(item,self.conf[item])

if __name__ =="__main__":
	pass
