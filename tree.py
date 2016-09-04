from treenode import TreeNode

class Tree:
	def __init__(self):
		self.nodes = []
		self.length = 0
		self.count = 0

	def nodes(self):
		return self.nodes

	def __repr__(self):
		return str(self.nodes)

	def __len__(self):
		return self.length

	def addNode(self, node):
		self.nodes.append(node)

	def createNode(self, state, op, path, parent=None):
		node = TreeNode(state, op, "N"+str(self.count), path, parent)
		self.count += 1
		return node

	def decreaseCount(self):
		self.count -= 1

	def incLength(self):
		self.length += 1

	def hasNode(self, target):
		if target in self.nodes:
			return True
		else:
			return False