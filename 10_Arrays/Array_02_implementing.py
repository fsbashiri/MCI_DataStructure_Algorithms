class MyArray:
    # constructor
    def __init__(self) -> None:
        self.length = 0
        self.data = {}
        pass

    # for printing the array
    def __str__(self):
        return str(self.__dict__)
        
    # get the item at the given index: O(1)
    def get(self, index):
        return self.data[index]

    # push the item at the end of the array: O(1)
    def push(self, item):
        self.data[self.length] = item
        self.length += 1
        return len(self.data)

    # pop the last item from the array: O(1)
    def pop(self):
        last_item = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return last_item

    # delete the item at the given index: O(n)
    def delete(self, index):
        item = self.data[index]
        self.shift_items(index)
        return item

    # shift items to the left
    def shift_items(self, index):
        for i in range(index, self.length - 1):
            self.data[i] = self.data[i + 1]
        del self.data[self.length - 1]
        self.length -= 1
        return

newArray = MyArray()
newArray.push('hi')
newArray.push('you')
newArray.push('!')
newArray.delete(1)
newArray.push('are')
newArray.push('nice')

print(newArray)