class Stack():
    def __init__(self) -> None:
        self.all = []
        self.length = 0
        pass
    
    def peek(self):
        # look at the top node
        if self.is_empty():
            return None
        return self.all[self.length - 1]

    def push(self, data):
        # add to the top of the stack
        self.all.append(data)
        self.length += 1
        return self

    def pop(self):
        # remove from the top of the stack
        if self.is_empty():
            return None
        self.all.pop()
        self.length -= 1
        return self

    def is_empty(self):
        # check if the stack is empty
        if self.length == 0 or not self.all:
            return True
        return False

    def __str__(self) -> str:
        return str(self.__dict__)


myStack = Stack()
myStack.push('Google')
myStack.push('Udemy')
myStack.push('Discord')
print(myStack.peek())
print(myStack.pop())
print(myStack)
