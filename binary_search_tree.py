class Node(object):
	def __init__(self, data = None):
		self.parent = None
		self.left = None
		self.right = None
		self.data = data

	@staticmethod
	def at_left(parent, child):
		return True if parent.left is child else False

	@staticmethod
	def has_left(node):
		return True if node.left else False

	@staticmethod
	def has_right(node):
		return True if node.right else False

	@staticmethod
	def is_empty(node):
		return True if (node == None) is None else False

class BinarySearchTree(object):
	def __init__(self, value, capacity = 30):
		self.size = 1
		self.capacity = capacity
		self.root = Node(data = value)

		self.root.parent = self.root
		self.last = None

	def add(self, value):
		node = Node(data = value)
		current_node = self.root

		if self.size >= self.capacity:
			if self.capacity <= 2000:
				self.capacity += self.capacity

			else:
				print('Maximum tree depth reached')

		self.last = node

		while True:
			if value < current_node.data:
				if not Node.has_left(current_node):
					node.parent = current_node
					current_node.left = node
					self.size += 1

					del node
					return

				current_node = current_node.left

			elif value > current_node.data:
				if not Node.has_right(current_node):
					node.parent = current_node
					current_node.right = node
					self.size += 1

					del node
					return

				current_node = current_node.right

	@staticmethod
	def extrema(node, mini = True):
		while node:
			previous = node
			node = node.left if mini else node.right
		else:
			return previous

	def find(self, value):
		current_node = self.root

		while True:
			if current_node.data == value:
				return current_node

			elif value < current_node.data :
				current_node = current_node.left

			elif value > current_node.data:
				current_node = current_node.right

			if current_node is None:
				break

		print('Value not found!')
		return

	@classmethod
	def from_list(cls, data_list):
		tree = BinarySearchTree(value = data_list[0], capacity = len(data_list))

		for data in data_list[1:]:
			tree.add(value = data)

		return tree

	def inorder_trav(self, node):
		if not node:
			return

		self.inorder_trav(node.left)
		print(node.data, end = ' ')
		self.inorder_trav(node.right)

	def levelorder_trav(self, node):
		nodes = [node]

		for node in nodes:
			print(node.data)
			if Node.has_left(node):
				nodes.append(node.left)

			if Node.has_right(node):
				nodes.append(node.right)				

		return

	def postorder_trav(self, node):
		if not node:
			return

		self.postorder_trav(node.left)
		self.postorder_trav(node.right)
		print(node.data)

	def preorder_trav(self, node):
		if not node:
			return

		print(node.data)
		self.preorder_trav(node.left)
		self.preorder_trav(node.right)

	@staticmethod
	def process_remove(home, at):
		if Node.at_left(parent = home.parent, child = home):
			home.parent.left = at
		else:
			home.parent.right = at
			
		if at:
			at.parent = home.parent

		return

	def remove(self, value):
		node = self.find(value)

		if node:
			if Node.has_left(node) and Node.has_right(node):
				at = BinarySearchTree.extrema(node.right)
				node.data, at.data = at.data, node.data

				BinarySearchTree.remove_modes(at)

			else:
				BinarySearchTree.remove_modes(node)

		return

	@staticmethod
	def remove_modes(node):
		if Node.has_left(node):
			BinarySearchTree.process_remove(home = node, at = node.left)

		elif Node.has_right(node):
			BinarySearchTree.process_remove(home = node, at = node.right)

		else:
			BinarySearchTree.process_remove(home = node, at = None)

		return


tree2 = BinarySearchTree.from_list(
	[5, 3, 1, -1, 26, 45, 33, 17, 2, -15, -7])
tree2.inorder_trav(tree2.root)