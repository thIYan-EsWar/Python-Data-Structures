from math import inf

class Node(object):
	def __init__(self, data = None):
		self.parent = None
		self.left = None
		self.right = None
		self.data = data

class PQueue(object):
	def __init__(self, value, capacity):
		self.capacity = capacity
		self.root = Node(data = value)

		self.list = [self.root]

	def bubble_down(self, node):
		while node.left or node.right:	# To check that there is actually a
										# next node to move  down 
			
			node2 = PQueue.next_node_down(node = node)
			if node is node2:
				return

			else:
				PQueue.swap_nodes(parent = node, child = node2)
				
			node = node2

		else:
			return

	def bubble_up(self, node):
		# To bubble up the newly added node at the left most corner
		# such that binary heap invariant is always satisfied					
		
		while not (node is self.root):			
			if PQueue.is_in_place(node):
				return 

			else:
				PQueue.swap_nodes(parent = node.parent, child = node)
				node = node.parent

		else:
			return

	def clear(self):
		del self.list[:]

	def dequeue(self):
		PQueue.swap_nodes(self.root, self.list[-1])
		last = self.list.pop()

		if PQueue.is_left(last):		# Removing the last node(swapped from
			last.parent.left = None 	# the root node) in order perform 
										# polling.
		else:
			last.parent.right = None

		self.bubble_down(self.root)

		return

	def enqueue(self, value):
		length = len(self.list)
		node = Node(data = value)

		if length < self.capacity:
			if length % 2 != 0:
				index = (length - 1) // 2		# Finding the index of the 
				self.list[index].left = node 	# parent node to which new
												# node will be made as a  
			else:								# left or right child based
				index = (length - 2) // 2		# on whether the index of the
				self.list[index].right = node 	# new node

			node.parent = self.list[index]
			self.list.append(node)

			self.bubble_up(node)

		else:
			print('Queue exhausted!')

		return

	def find(self, value):
		data_list = self.list_data()

		if value in data_list:
			return [index for index in range(len(data_list)) \
					if data_list[index] == value]

		else:
			print('Value not found!')
			return


	def list_data(self):
		return [item.data for item in self.list]

	@classmethod
	def from_list(cls, values):
		queue = cls(value = values[0], capacity = len(values))

		for value in values[1:]:
			queue.enqueue(value = value)

		return queue

	@staticmethod
	def is_in_place(node):
		return True if node.data >= node.parent.data else False

	@staticmethod
	def is_left(node):
		return True if node is node.parent.left else False

	@staticmethod
	def next_node_down(node):
		"""
			To get the next node while swimming down the nodes. This gives 
		the next smallest valued node, if any. If no node is smaller than the
		given node, then this returns the node itself. 

		### Note: For any given node in a binary heap there may or may not be
		a right node, so it is safe to assign it to positive infinty if the 
		heap is a min heap, else assigned to negative infinity. 
		"""
		if node.data > node.left.data and node.data > (node.right.data or inf):
			return node.left if node.left.data <= node.right.data \
							else node.right 

		elif node.data > node.left.data:
			return node.left

		elif node.data > (node.right.data or inf):
			return node.right

		else:
			return node

	def remove(self, value):
		data_list = self.list_data()

		if value == data_list[0]:
			self.dequeue()
			return

		if value in data_list:
			index = data_list.index(value)

			PQueue.swap_nodes(parent = self.list[index], child = self.list[-1])
			removing = self.list.pop()

			if PQueue.is_left(removing):
				removing.parent.left = None

			else:
				removing.parent.right = None

			del removing

			current_node = self.list[index]

			if PQueue.is_in_place(current_node):
				self.bubble_down(current_node)

			else:
				self.bubble_up(current_node)

		else:
			print('Value not found')
			return

	@staticmethod
	def swap_nodes(parent, child):
		parent.data, child.data = child.data, parent.data
