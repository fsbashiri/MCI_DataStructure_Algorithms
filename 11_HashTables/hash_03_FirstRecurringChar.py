# Google Question
# Given an array = [2,5,1,2,3,5,1,2,4]:
# It should return 2

# Given an array = [2,1,1,2,3,5,1,2,4]:
# It should return 1

# Given an array = [2,3,4,5]:
# It should return undefined

# using arrays: time complexity O(n^2) - space complexity O(1)
def firstRecurringChar1(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                return arr[i]
    return None

# revised first version to return first recurring pair
def firstRecurringChar2(arr):
    for i in range(1, len(arr)):
        for j in range(0, i):
            if arr[i] == arr[j]:
                return arr[i]
    return None

# using hash table: time complexity O(n) - space complexity O(n)
def firstRecurringChar3(arr):
    # create a hash table
    hash_table = {}
    # loop through the array
    for c in arr:
        if c in hash_table:
            return c
        else:
            hash_table[c] = True
    return None
    

# array = [2,5,1,2,3,5,1,2,4]
# array = [2,1,1,2,3,5,1,2,4]
# array = [2,3,4,5]
array = [2,5,5,2,3,5,1,2,4]  # return 5 because the pairs are before 2,2
print(firstRecurringChar1(array))
print(firstRecurringChar2(array))
print(firstRecurringChar3(array))
