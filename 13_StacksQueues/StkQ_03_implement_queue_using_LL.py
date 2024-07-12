class Node():
    def __init__(self, value) -> None:
        self.data = value
        self._next = None
        pass

    def __str__(self) -> str:
        return str(self.__dict__)

    def __repr__(self) -> str:
        return f"Node({self.data})"

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, value):
        self._next = value


class Queue():
    def __init__(self) -> None:
        self.first = None
        self.last = None
        self.length = 0
        pass

    def peek(self):
        # look at the first in line
        return self.first

    def enqueue(self, value):
        # add to the end of the line
        newNode = Node(value)
        if self.length == 0:
            self.first = newNode
            self.last = newNode
        else:
            self.last.next = newNode
            self.last = newNode
        self.length += 1
        return self

    def dequeue(self):
        # remove from the beginning of the line
        if self.is_empty():
            return None
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
        self.length -= 1
        return self

    def __str__(self) -> str:
        return str(self.__dict__)

    def is_empty(self):
        return (self.length == 0 or self.first is None)

    def printt(self):
        # print the queue
        currNode = self.first
        while currNode is not None:
            print(currNode.data, end=' -> ')
            currNode = currNode.next
        print('End')


myQueue = Queue()
myQueue.enqueue('Joy')
myQueue.enqueue('Matt')
myQueue.enqueue('Pavel')
myQueue.enqueue('Samir')
print(myQueue.peek())
myQueue.dequeue()
myQueue.dequeue()
myQueue.dequeue()
myQueue.dequeue()
print(myQueue)
myQueue.printt()
