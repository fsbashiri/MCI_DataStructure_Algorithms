class HashTable:
    def __init__(self, size):
        self.size = size
        # self.data = [[] * 2] * self.size  # terrible way to create an empty list
        self.data = [[] * 2 for i in range(self.size)]
        
    def _hash(self, key):  # O(1)
        hash = 0
        for i, c in enumerate(key):
            hash  = (hash + ord(c) * i) % self.size
        return hash

    def set(self, key, value):  # O(1)
        address = self._hash(key)
        # a necessary if statement when data is initialized this way: 
        # [[] * 2] * self.size due to the way python handles list creation
        # if not self.data[address]:
        #     self.data[address] = []
        # check if key already exists
        # bucket = self.data[address]
        # for i in range(len(bucket)):
        #     if bucket[i][0] == key:
        #         bucket[i][1] = value
        #         return None
        self.data[address].append([key, value])
        return None

    def get(self, key):  # O(1) with a good hash function and large-enough data
        address = self._hash(key)
        currentBucket = self.data[address]
        if currentBucket:
            for i in range(len(currentBucket)):
                if currentBucket[i][0] == key:
                    return currentBucket[i][1]
        return None

    def keys(self):
        keysArray = []
        # loop through all the buckets
        for i in range(self.size):
            # if not empty
            if self.data[i]:
                # loop through all the key-value pairs in the bucket
                for j in range(len(self.data[i])):
                    keysArray.append(self.data[i][j][0])
        return keysArray


myHashTable = HashTable(50)
print(myHashTable._hash('grapes'))
myHashTable.set('grapes', 5)
myHashTable.set('apples', 10)
myHashTable.set('oranges', 20)
print(myHashTable.data)
print(myHashTable.get('grapes'))
print(myHashTable.keys())
