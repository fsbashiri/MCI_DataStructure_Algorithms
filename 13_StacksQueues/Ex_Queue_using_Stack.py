class MyQueue_1:
    def __init__(self):
        self.s1 = []  # keeps the items in the queue in reversed order; s1 = [3, 2, 1]
        self.s2 = []  # used in push operation to keep the items in reversed order
    
    def push(self, x: int) -> None:
        while len(self.s1) > 0:
            self.s2.append(self.s1.pop())
        self.s1.append(x)
        while len(self.s2) > 0:
            self.s1.append(self.s2.pop())
        return
    
    def pop(self) -> int:
        return self.s1.pop()
    
    def peek(self) -> int:
        if len(self.s1) == 0:
            return None
        return self.s1[-1]
    
    def empty(self) -> bool:
        return len(self.s1) == 0


class MyQueue_2:
    def __init__(self):
        self.pushStack = []
        self.popStack = []

    def push(self, x: int) -> None:
        self.pushStack.append(x)
        return

    def pop(self) -> int:
        if self.empty():
            return None
        if self.popStack:
            return self.popStack.pop()
        while self.pushStack:
            self.popStack.append(self.pushStack.pop())
        return self.popStack.pop()

    def peek(self) -> int:
        if self.empty():
            return None
        if not self.popStack:
            return self.pushStack[0]
        else:
            return self.popStack[-1]

    def empty(self) -> bool:
        return (len(self.pushStack) == 0) and (len(self.popStack) == 0)

# Your MyQueue object will be instantiated and called as such:
obj = MyQueue_2()
obj.push(1)
obj.push(2)
print(obj.pop())
print(obj.peek())
print(obj.empty())