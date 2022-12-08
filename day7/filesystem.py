
class File:
	def __init__(self, filename, size):
		self.name = filename
		self.size = size

class Dir:
	def __init__(self, dirname, parent=None):
		self.name = dirname
		self.parent = parent
		self.children = []
		self.files = []
		self.size = None

	def addChild(self, child):
		self.children.append(child)

	def addFile(self, file):
		self.files.append(file)

	def getChild(self, childname):
		for c in self.children:
			if c.name == childname:
				return c
		raise Exception("Directory not found!")

	def getSize(self):
		if self.size != None:
			return self.size
		res = sum(map(lambda x: x.size, self.files))
		for child in self.children:
			res += child.getSize()
		self.size = res
		return res