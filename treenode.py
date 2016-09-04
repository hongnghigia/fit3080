class TreeNode:
	def __init__(self, state, op, identifier, path, parent = None):
		self.children = []
		self.op = op
		self.state = state
		self._identifier = identifier
		self.parent = parent
		self.path = path + [self._identifier]

	def isRoot(self):
		return not self.parent

	def hasChildren(self):
		if len(self.children) == 0:
			return False
		else:
			return True


	def __repr__(self):
		return self.state

	@property
	def identifier(self):
		return self._identifier

	def getParent(self):
		return self.parent
		
	
	def addChild(self, identifier):
		self.children.append(identifier)

	def getState(self):
		return self.state

	def getChildren(self):
		return self.children

	def getOp(self):
		return self.op

	def getPath(self):
		return self.path

	def addPath(self, node):
		self.path.append(node)

