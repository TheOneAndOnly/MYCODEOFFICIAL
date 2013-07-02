#Stacks and queues
#should empty stack and end queues

class Queue:
        
    def __init__(self):
        self.elements = []
        
    def insert(self,thing):
        self.elements.append(thing)

    def remove(self):
        if len(self.elements) == 0:
            print "The queue is empty."
            return
        print self.elements[0]
        self.elements.pop(0)


queue = Queue()
queue.insert(14)
queue.insert(8)
queue.remove()
queue.insert(7)
queue.remove()


class Stack():

    def __init__(self):
        self.elements = []

    def push(self, item):
        self.elements.append(item)

    def pop(self):
        if len(self.elements) == 0:
            print "The stack is not full."
            return
        print self.elements[len(self.elements)-1]
        del self.elements[len(self.elements)-1]

#should print numbers?
stack = Stack()
stack.push(5)
stack.push(6)
stack.pop()
stack.push(7)
stack.pop()
stack.pop()
stack.pop()

#please don't copy this code but use it for educational use's



        
        
        
