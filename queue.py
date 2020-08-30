# Functions - enqueue, dequeue, peek

# Implement with list
# Assumptions: Start of Queue @ idx 0; End of list at the back
class Queue(object):
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]


# Implement with linked list
# Assumptions: Start of Queue at head node; End of queue at tail

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue_ll(object):

    def __init__(self):
        self.front = None
        self.back = None

    def enqueue(self, item):
        if self.front == None:
            self.front = Node(item)
            self.back = Node(item)
        else:
            self.back.next = Node(item)
            self.back = Node(item)


# Test1 - List implementation
# line = Queue()
# print(line.items)

# line.enqueue('a')
# line.enqueue('b')
# line.enqueue('c')
# line.enqueue('d')
# print(line.items)

# print(line.dequeue())

# print(line.peek())

# Test2 - Linked List implementation
line = Queue_ll()
# print(line)
# print(line.front)
# print(line.back)

line.enqueue('a')
line.enqueue('b')
# line.enqueue('c')
print(line.front.data)
print(line.front.next.data)
# print(line.back.data)