class Node:
    def __init__(self, value) -> None:
        self.data = {
            'value': value,
            'next': None,
            'prev': None
        }
    pass


class DoublyLinkedList:
    def __init__(self, value) -> None:
        newNode = Node(value)
        self.head = newNode.data
        self.tail = newNode.data
        self.length = 1
    pass

    def append(self, value):
        newNode = Node(value)
        newNode.data['prev'] = self.tail
        self.tail['next'] = newNode.data
        self.tail = newNode.data
        self.length += 1
        return self

    def prepend(self, value):
        newNode = Node(value)
        newNode.data['next'] = self.head
        self.head['prev'] = newNode.data
        self.head = newNode.data
        self.length += 1
        return self

    def traverseToIndex(self, index):
        # check params
        if index >= self.length or index < 0:
            print('Index out of range')
            return None
        # traverse
        counter = 0
        currNode = self.head
        while counter != index:
            currNode = currNode['next']
            counter += 1
        return currNode
        
    def insert(self, index, value):
        newNode = Node(value)
        if index > self.length or index < 0:
            print('Index out of range')
            return self
        elif index == 0:
            self.prepend(value)
            return self
        elif index == self.length:
            self.append(value)
            return self
        else:
            leader = self.traverseToIndex(index - 1)
            if leader is not None:
                newNode.data['next'] = leader['next']
                newNode.data['prev'] = leader
                leader['next']['prev'] = newNode.data
                leader['next'] = newNode.data
                self.length += 1
            return self

    def remove(self, index):
        # check params
        if index >= self.length or index < 0:
            print('Index out of range')
            return self
        # remove index
        if index == 0:
            self.head = self.head['next']
            if self.head is not None:
                self.head['prev'] = None
            # update tail if length == 1
            if self.length == 1:
                self.tail = self.head
            self.length -= 1
        else:
            leader = self.traverseToIndex(index - 1)
            if leader is not None:
                unwanted_node = leader['next']
                follower = unwanted_node['next']
                leader['next'] = follower
                if follower is not None:
                    follower['prev'] = leader
                # update tail
                if index == self.length - 1:
                    self.tail = leader
                # update length
                self.length -= 1
        return self

    def __str__(self) -> str:
        return str(self.__dict__)


myDoublyLL = DoublyLinkedList(5)
myDoublyLL.append(10)
myDoublyLL.prepend(1)
# myDoublyLL.insert(1, 99)
myDoublyLL.remove(0)

print(myDoublyLL)