class ConfigReader():
	def __init__(self, name = "config.txt"):
		self.keys = {}
		self.name = name

	#Read Keys from file
	def readKeys(self):
		keysFile = open(self.name,"r")
		lines = [line.rstrip() for line in keysFile]
		keysFile.close()
		self.keys.clear()
		for item in lines:
			#If there's nothing on the line, ignore it.
			if len(item) == 0:
				continue
			#If a commented line, ignore it
			if item[0] == "#":
				continue
			#If a new line is the first char, ignore it.
			elif item[0] == "\n":
				continue

			else:
				pos = item.find("=")
				if pos != -1 and pos != len(item)-1:
					#Name of the key is [0:pos], Value of the key is [pos+1:], unless we have "foo = bar" rather than "foo=bar", where it will be [pos2:] for the latter argument
					if item[pos-1] == " " and item[pos+1] == " ":
						self.keys[item[0:pos-1]] = item[pos+2:]
					else:
						self.keys[item[0:pos]]=item[pos+1:]
					

	#Return the keys, read allows you to get the keys without re-reading the file.
	def getKeys(self, read=True):
		if read:
			self.readKeys()
		return self.keys
			
