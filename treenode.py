class TreeNode:
	def __init__(self, state, identifier, parent = None):
		self.children = []
		self.state = state
		self._identifier = identifier
		self.parent = parent

	def isRoot(self):
		return not self.parent

	def hasChildren(self):
		if len(self.children) == 0:
			return False
		else:
			return True


	@property
	def identifier(self):
		return self._identifier
	
	def addChild(self, identifier):
		self.children.append(identifier)

	def getState(self):
		return self.state
