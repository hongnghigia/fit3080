class Node:
	def __init__(self, string, op, identifier, cost, path, parent):
		self.string = string
		self.op = op
		self.g = cost
		self.f = 0
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


	def heuristic(self):
		count = 0
		for i in range(0,3):
			if self.string[i] == "B":
				count += 2

		self.h = count

		self.f = self.h + self.g
		return self.f
