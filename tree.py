from treenode import Node

class Tree:
	def __init__(self):
		self.count = 0

	def makeNode(self, string, op, cost, path, parent):

		if op == 3 or op == -3:
			cost += 2
		else:
			cost += 1 

		node = Node(string, op, "N"+str(self.count), cost, path, parent)
		self.count += 1

		return node