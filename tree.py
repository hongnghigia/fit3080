from treenode import TreeNode

class Tree:
	def __init__(self):
		self.nodes = []
		self.length = 0
		self.identifier = 0

	def nodes(self):
		return self.nodes

	def getLength(self):
		return self.length

	def __len__(self):
		return self.length

	def addNode(self, node):
		self.identifier += 1
		self.nodes.append(node)

	def createNode(self,state,identifier,parent=None):
		node = TreeNode(state, identifier+str(self.identifier), parent)

		return node