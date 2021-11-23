class StaticArray(object):
	def __init__(self, length = 0):
		self.__length = length
		assert type(length) == int, TypeError
		assert 0 <= length <= 1000, AssertionError
		self.__array = [None] * length

	def append(self, value):
		try:
			index = self.__array.index(None)
			self.__array[index] = value
			return 0
		except Exception as e:
			if str(e) == 'None is not in list':
				print('Index not found!')
		else:
			return -1

	def clear(self):
		self.__array.clear()

		return 

	def describe(self, print_description = True):
		index = self.__array.index(None)
		array = self.__array[0:index]

		if print_description:
			print(f'Array ID: {id(self.__array)}\nMaximum length: {self.__length}\nUnallocated: {self.__length - index}\nContents: {array}')
		
		return self.__length, array

	def insert(self, pos, value):
		assert type(pos) == int, TypeError
		assert 0 <= pos <= self.__length, IndexError
		
		self.__array[pos - 1] = value

	def pop(self, index):
		assert type(index) == int, TypeError
		assert 0 <= index < self.__length, IndexError

		return self.__array.pop(index)

	def remove(self, value):
		try:
			self.__array.remove(value)
		except Exception as e:
			print(str(e))




