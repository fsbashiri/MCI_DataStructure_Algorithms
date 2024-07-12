class Node():
    def __init__(self, data) -> None:
        self.data = data
        self._next = None  # private attribute, because its partly initialized (set to None)
    pass

    def __str__(self) -> str:
        return str(self.__dict__)

    def __repr__(self) -> str:
        return f"Node({self.data})"

    @property  # property decorator makes it a Read-Only attribute
    def next(self):
        return self._next

    @next.setter  # special decorator to let user change the value of the attribute
    def next(self, value):
        self._next = value


class Stack():
    def __init__(self) -> None:
        self.top = None
        self.bottom = None
        self.length = 0
        pass
    
    def peek(self):
        # look at the top node
        return self.top

    def push(self, data):
        # add to the top of the stack
        newNode = Node(data)
        if self.length == 0:
            self.top = newNode
            self.bottom = newNode
        else:
            newNode.next = self.top
            self.top = newNode
        self.length += 1
        return self

    def pop(self):
        # remove from the top of the stack
        if self.is_empty():
            return None
        if self.length == 1:
            self.top = None
            self.bottom = None
        else:
            self.top = self.top.next
        self.length -= 1
        return self

    def is_empty(self):
        # check if the stack is empty
        if self.length == 0 or self.top is None:
            return True
        return False

    def __str__(self) -> str:
        return str(self.__dict__)

    def printt(self):
        # print the stack
        currNode = self.top
        while currNode is not None:
            print(currNode.data, end=' -> ')
            currNode = currNode._next
        print()
        return


myStack = Stack()
myStack.push('Google')
myStack.push('Udemy')
myStack.push('Discord')
print(myStack.peek())
print(myStack.pop())
print(myStack)
myStack.printt()
