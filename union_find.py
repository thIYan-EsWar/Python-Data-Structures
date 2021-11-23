class Node(object):
	def __init__(self, data = None):
		self.parent = None
		self.previous = None

		self.data = data

class UnionFind(object):
	def __init__(self, data_list):
		self.size = len(data_list)
		self.list = {}

		self.groups = self.size

		self.count = 0
		for data in data_list:
			self.list[count] = Node(data = data)
			current_node = self.list[count]

			current_node.parent = current_node
			current_node.previous = current_node.parent

			self.count += 1

	def find(self, node):
		count = 0

		while not (node.parent is node):
			count += 1
			node = node.parent

		else:
			return node, count

	def union(self, index1, index2):
	 	if index1 >= self.size and index2 >= self.size:
	 		print('Index out of bound!')
	 		return

	 	node1, node2 = self.list[index1], self.list[index2]

	 	root_1, number_of_components_1 = self.find(node1)
	 	root_2, number_of_components_2 = self.find(node2)

	 	if root_1 is root_2:

	 		if not node2.previous is root_1:
	 			node2.parent = root_1
	 			node2.previous = root_1

	 		return

	 	else:
	 		self.groups -= 1

	 		if number_of_components_1 >= number_of_components_2:
	 			root_2.parent = root_1
	 			root_2.previous = root_1

	 			node2.parent = root_1
	 			node2.previous = root_1

	 		else:
	 			root_1.parent = root_2
	 			root_1.previous = root_1

	 			node1.parent = root_2
	 			node1.previous = root_2

	 			return

	def groups(self):
		return self.groups