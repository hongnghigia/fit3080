class Node:
	def __init__(self, string, op, identifier, cost, path, parent):
		self.string = string
		self.op = op
		self.g = 0
		self.h = 0
		self.identifier = identifier
		self.cost = cost
		self.parent = parent
		self.path = path + [self.identifier]

	def __repr__(self):
		return self.identifier


	def getState(self):
		return self.string


	def getOp(self):
		return self.op


	def getCost(self):
		return self.cost


	def getPath(self):
		return self.path


	def getString(self):
		return self.string


	def getParent(self):
		return self.parent