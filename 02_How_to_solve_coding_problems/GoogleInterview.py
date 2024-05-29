# You are given an array and an int. Find pairs of elements in the array that sum to the int.

arr = [1, 2, 3, 4, 4]
sum = 8

# Naive: O(n^2)
def hasPairWithSum(arr, sum):
    arrLen = len(arr)
    for i in range(arrLen):
        for j in range(i+1, arrLen):
            if arr[i] + arr[j] == sum:
                return True
    return False

# print('Solution 1: ' + str(hasPairWithSum(arr, sum)))

# Better: O(n) - Sorted array only
def hasPairWithSum2(arr, sum):
    low = 0
    hi = len(arr) - 1
    while (low < hi):
        s = arr[low] + arr[hi]
        if s == sum:
            return True
        elif s < sum:
            low += 1
        elif s > sum:
            hi -= 1
    return False

# print('Solution 2: ' + str(hasPairWithSum2(arr, sum)))

    
# Better: O(n) - not sorted array
def hasPairWithSum3(arr, sum):
    mySet = set()
    arrLen = len(arr)
    for i in range(arrLen):
        if arr[i] in mySet:
            return True
        mySet.add(sum - arr[i])
    return False

print('Solution 3: ' + str(hasPairWithSum3(arr, sum)))