# 10-->5-->16

# myLinkedList = {
#     'head': {
#         'value' : 10,
#         'next' : {
#             'value' : 5,
#             'next' : {
#                 'value' : 16,
#                 'next' : None
#             }
#         }
#     }
# }

class Node:
    def __init__(self, value):
        # self.value = value
        # self.next = None
        self.data = {
            'value' : value,
            'next' : None
        }

class LinkeList:
    def __init__(self, value) -> None:
        self.head = {
            'value' : value,
            'next' : None
        }
        self.tail = self.head
        self.length = 1
        pass
    
    def append(self, value):
        # newNode = {
        #     'value' : value,
        #     'next' : None
        # }
        newNode = Node(value=value)
        self.tail['next'] = newNode.data
        self.tail = newNode.data
        self.length += 1
        return self

    def prepend(self, value):
        # newNode = {
        #     'value' : value,
        #     'next' : None
        # }
        newNode = Node(value=value)
        newNode.data['next'] = self.head
        self.head = newNode.data
        self.length += 1
        return self

    def traverseToIndex(self, index):
        # check param
        if index >= self.length:
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
        if index > self.length:
            print('Index out of range')
            return self
        elif index == 0:
            self.prepend(value)
            return self
        elif index == self.length:
            self.append(value)
            return self
        else:
            leader = self.traverseToIndex(index-1)
            if leader is not None:
                newNode.data['next'] = leader['next']
                leader['next'] = newNode.data
                self.length += 1
            return self

    def remove(self, index):
        # check params
        if index >= self.length or index < 0:
            print('Index out of range')
            return self
        # remove index
        leader = self.traverseToIndex(index-1)
        if leader is not None:
            leader['next'] = leader['next']['next']
            # update tail
            if index == self.length - 1:
                self.tail = leader
            # update length
            self.length -= 1
        return self

    def reverse(self):
        if self.length == 1:
            return self
        else:
            first = self.head
            second = first['next']
            self.head = self.tail
            self.tail = first
            self.tail['next'] = None
            while second is not None:
                temp = second['next']
                second['next'] = first
                first = second
                second = temp
            return self

    def __str__(self) -> str:
        return str(self.__dict__)


myLinkedList = LinkeList(10)
myLinkedList.append(5)
myLinkedList.append(16)
myLinkedList.prepend(1)
myLinkedList.insert(1, 99)
myLinkedList.insert(20, 88)
myLinkedList.remove(1)
myLinkedList.reverse()

print(myLinkedList)