class TreeNode:
	def __init__(self, parent=None, state, identifier):
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
	
	def add_child(self, identifier):
		self.children.append(identifier)