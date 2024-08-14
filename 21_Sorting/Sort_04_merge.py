# Time complexit: O(n log n) - uses recursion
def mergeSort(array):
    if len(array) == 1:
        return array
        
    # Split Array into right and left
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]
    # print(f"left: {left}")
    # print(f"right: {right}")
    
    return merge(
        mergeSort(left),
        mergeSort(right)
    )

def merge(left, right):
    # code here
    result = []
    leftIndex = 0
    rightIndex = 0
    while leftIndex < len(left) and rightIndex < len(right):
        if left[leftIndex] < right[rightIndex]:
            result.append(left[leftIndex])
            leftIndex += 1
        else:
            result.append(right[rightIndex])
            rightIndex += 1
    # print(f"merge: {result + left[leftIndex:] + right[rightIndex:]}")
    return result + left[leftIndex:] + right[rightIndex:]


numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

print(numbers)
numbers = mergeSort(numbers)
print(numbers)
