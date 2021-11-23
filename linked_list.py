class Node(object):
	"""
	This class is the node for the list. 
	* This class has 2 attributes
		1. next -> points to the next node
		2. data -> gives the value stored in a node 
	"""
	def __init__(self, data = None, next_object = None):
		self.data = data
		self.next = next_object

class SinglyLinkedList(object):
	"""
	This class creates a template to a doubly linked list
	"""
	def __init__(self):
		"""
		* initializes a new node as head and tail of a list
		"""
		self.head = Node()
		self.tail = Node()

		self.head.next = self.tail
		
		self.__length = 0

	def append(self, value):
		"""
		* adds a new node at the end of the list
		* keeps track of the length of the list
		"""
		self.__length += 1
		
		node = Node(data = value)
		
		if self.head.data == None:
			self.head = node
			node.next = self.tail

		else:
			current_node = self.head
			next_node = current_node.next

			while not next_node is self.tail:
				current_node = next_node
				next_node = current_node.next
			else:
				current_node.next = node
				node.next = self.tail

	def first(self):
		"""
		* returns the head of the list
		"""
		return self.head
	
	def head_start(self, value):
		"""
		* replaces a node with the value given
		"""
		node = Node(data = value)

		current_node = self.head
		self.head = node
		node.next = current_node

	def length(self):
		"""
		* returns the length of the list
		"""
		return self.__length

	def remove(self, value):
		"""
		* removes a paritcular value at a node
		"""
		previous_node = None
		current_node = self.head

		while current_node.data:
			if current_node.data == value:
				previous_node.next = current_node.next
				del current_node
				return
			else:
				previous_node = current_node
				current_node = current_node.next

		else:
			return

	def seek(self, value):
		"""
		* seeks for a particular value in the list
		"""
		current_node = self.head

		while current_node.data:
			if current_node.data == value:
				return current_node

			else:
				current_node = current_node.next

		else:
			return