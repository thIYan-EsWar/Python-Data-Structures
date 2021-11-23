class Node(object):
	def __init__(self, previous = None, next_obj = None, data = None):
		self.previous = previous
		self.next = next_obj
		self.data = data

class Queue(object):
	def __init__(self):
		self.__head = Node()
		self.__tail = Node()

		self.__head.next = self.__tail
		self.__tail.previous = self.__head

		self.__length = 0

	def dequeue(self):
		if not self.__length == 0:
			self.__length -= 1
			head = self.__head

			self.__head = head.next
			self.__head.next = head.next.next

			del head

			return

		else:
			print('Empty stack!')
			return 

	def enqueue(self, value):
		node = Node(data = value)
		self.__length += 1

		if not self.__head.data:
			self.__head = node
			node.next = self.__tail
			self.__tail.previous = node

			return

		else:
			previous = self.__tail.previous
			previous.next = node
			node.previous = previous

			node.next = self.__tail
			self.__tail.previous = node

			return

	def head(self):
		return self.__head

	def is_empty(self):
		return True if self.__length == 0 else False

	def length(self):
		return self.__length

	def remove(self, value):
		if not self.is_empty():
			current_node = self.__head

			while current_node.data:
				if current_node.data == value:
					current_node.previous.next = current_node.next
					current_node.next.previous = current_node.previous

					del current_node

					return

				current_node = current_node.next
			else:
				print(f'Value({value}) not found in the queue.')
				return

		else:
			print('Empty stack!')
			return

	def seek(self, value):
		if not self.is_empty():
			current_node = self.__head

			while current_node.data:
				if current_node.data == value:
					return current_node

				current_node = current_node.next
			else:
				print(f'Value({value}) not found in the queue.')
				return

		else:
			print('Empty stack!')
			return

	def tail(self):
		return self.__tail