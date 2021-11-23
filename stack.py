class Node(object):
	def __init__(self, previous = None, next_obj = None, data = None):
		self.previous = previous
		self.next = next_obj

		self.data = data

class Stack(object):
	def __init__(self):
		self.head = Node()
		self.tail = Node()

		self.head.next = self.tail
		self.tail.previous = self.head

		self.__length = 0

	def is_empty(self):
		return True if self.__length == 0 else False

	def length(self):
		return self.__length

	def pop(self):
		if self.__length > 0:
			self.__length -= 1

			head = self.head
			self.head = head.next
			head.next.previous = self.head

			del head

		else:
			print('Empthy stack!')
			return

	def push(self, value):
		self.__length += 1

		node = Node(data = value)

		if self.__length == 0:
			self.tail = node

		else:
			head = self.head
			self.head = node
			node.next = head
			head.previous = node

	def seek(self, value):
		current_node = self.head
		length = self.__length

		while length:

			if current_node.data == value:
				return current_node

			else:
				current_node = current_node.next

			length -= 1

		else:
			print(f'Value({value}) not found in the stack!')
			return