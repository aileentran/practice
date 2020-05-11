"""
Create a queue using two stacks!
Create stack class: init, push, pop, peek

Create queue class: init, dequeue, enqueue, peek
FIRST IN, FIRST OUT! 
init: one stack is the actual queue and second stack is empty so we can move stuff from the actual queue arounnddd 
enqueue: just pushing stuff into actual queue
dequeue: pop items from queue into second stack until len(queue) is one. 
pop that baby off into the abyss. 
then repop from second stack into queue
peek: pop items from queue into second stack until len(queue) is one and return that 

"""
class Stack(object):

	def __init__(self):
		self.items = []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		if not self.items:
			return None

		return self.items.pop()

	def peek(self):
		if not self.items:
			return None

		return self.items[-1]

class Queue(object):

	def __init__(self):
		self.queue = Stack()
		self.second_stack = Stack()

	def enqueue(self, item):
		self.queue.push(item)

	def dequeue(self):

		# getting to very first item
		while len(self.queue.items) > 1:
			item = self.queue.pop()
			self.second_stack.push(item)

		dequeued = self.queue.pop()
		
		# requeueing the rest of the queue w/first item gone
		while len(self.second_stack.items) > 0:
			item = self.second_stack.pop()
			self.queue.push(item)

		return dequeued

	def peek(self):

		# getting very first item
		peekaboo = None

		while len(self.queue.items) > 1:
			item = self.queue.pop()
			self.second_stack.push(item)

		peekaboo = self.queue.pop()

		# requeue the queue!
		self.queue.push(peekaboo)

		while len(self.second_stack.items) > 0:
			stack_item = self.second_stack.pop()
			self.queue.push(stack_item)

		return peekaboo

a = Queue()
# a.enqueue(1)
# a.enqueue(2)
# a.enqueue(3)
print(a.dequeue())

    
