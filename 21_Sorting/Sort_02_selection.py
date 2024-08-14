# Time complexit: O(n^2)
def selectionSort(array):
    # Code here
    id = 0
    arrLen = len(array)
    for i in range(arrLen - 1):
        id = i
        for j in range(i+1, arrLen):
            if array[j] < array[id]:
                id = j
        # swap numbers
        array[i], array[id] = array[id], array[i]
    return array

numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

print(numbers)
selectionSort(numbers)
print(numbers)
