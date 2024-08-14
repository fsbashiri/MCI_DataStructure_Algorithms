# Time complexit: O(n log n)
def quickSort(array, left, right):
    # Code here
    if left < right:
        # partition the array
        pivot = partition(array, right, left, right)
        # sort the left and right
        quickSort(array, left, pivot-1)
        quickSort(array, pivot+1, right)   
    return array

def partition(array, pivot, left, right):
    # Code here
    # partition the array
    partitionIndex = left
    for j in range(left, right):
        if array[j] <= array[right]:
            swap(array, partitionIndex, j)
            partitionIndex += 1
    # move pivot to the right place
    swap(array, partitionIndex, right)
    return partitionIndex

def swap(array, firstIndex, secondIndex):
    # Code here
    if firstIndex == secondIndex:
        return
    temp = array[firstIndex]
    array[firstIndex] = array[secondIndex]
    array[secondIndex] = temp
    return


numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

print(numbers)
#Select first and last index as 2nd and 3rd parameters
quickSort(numbers, 0, len(numbers) - 1);
print(numbers)
