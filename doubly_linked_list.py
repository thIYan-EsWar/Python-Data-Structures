class Node(object):
	"""
	This class is the node for the list. 
	* This class has 3 attributes
		1. previous -> to get the previous node
		2. next -> points to the next node
		3. data -> gives the value stored in a node 
	"""
	def __init__(self, previous = None, next_obj = None, data = None):
		self.previous = previous
		self.next = next_obj
		self.data = data

class DoublyLinkedList(object):
	"""
	This class creates a template for a doubly linked list
	"""
	def __init__(self):
		"""
		* Inititalizes a node
		"""
		self.head = Node()
		self.tail = Node()

		self.__length = 0

		self.head.next = self.tail
		self.tail.previous = self.head

	def append(self, value):
		"""
		* appends a data to the list at the end
		* keeps track of the length of the list
		"""
		self.__length += 1

		node = Node(data = value)

		if self.head.data == None:
			self.head = node
			node.next = self.tail
			self.tail.previous = node

		else:
			tail = self.tail

			tail.previous.next = node
			node.previous = tail.previous

			node.next = tail
			tail.previous = node
			# #Alternate solution

			# current_node = self.head

			# while not current_node.next is self.tail:
			# 	current_node = current_node.next

			# else:
			# 	current_node.next = node
			# 	node.previous = current_node

			# 	node.next = self.tail
			# 	self.tail.previous = node

	def first(self):
		"""
		* returns the head node
		"""
		return self.head

	def head_start(self, value):
		"""
		* replaces the head node value with the value passed
		"""
		node = Node(data = value)
		current_node = self.head

		self.head = node
		node.next = current_node
		current_node.previous = node

	def length(self):
		# returns length of the list
		return self.__length

	def last(self):
		# retrun the tail node of the list
		return self.tail

	def remove(self, value):
		"""
		* remove a value present in a node of the list
		"""
		current_node = self.head

		while current_node.data:
			if current_node.data == value:
				current_node.previous.next = current_node.next
				current_node.next.previous = current_node.previous

				del current_node
				return
			else:
				current_node = current_node.next

		else:
			print(f'Value({value}) not found!')
			return

	def seek(self, value):
		"""
		This class creates a template to a doubly linked list
		"""
		current_node = self.head

		while current_node.data:
			if current_node.data == value:
				return current_node
			
			else:
				current_node = current_node.next
		else:
			print(f'Value({value}) not found!')
			return