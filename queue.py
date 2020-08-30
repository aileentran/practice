# Functions - enqueue, dequeue, peek

# Implement with list
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


# Cases
line = Queue()
print(line.items)

line.enqueue('a')
line.enqueue('b')
line.enqueue('c')
line.enqueue('d')
print(line.items)

print(line.dequeue())

print(line.peek())