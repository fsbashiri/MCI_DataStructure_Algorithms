# implementation 1: Time complexit: O(n^2)
# def insertionSort(array):
#     # Code here
#     arrLen = len(array)
#     for i in range(1, arrLen):
#         for j in range(i, 0, -1):
#             if array[j] < array[j-1]:
#                 # swap numbers
#                 array[j], array[j-1] = array[j-1], array[j]
#             else:
#                 break
#     return array

# Time complexit: O(n^2) - Best case: O(n)
def insertionSort(array):
    # Code here
    arrLen = len(array)
    for i in range(1, arrLen):
        # search for right spot only if number is smaller than the previous one
        if array[i] < array[i-1]:
            # compare with index 0
            if array[i] <= array[0]:
                # move number to the first position
                array[:i+1] = [array[i]] + array[:i]
            else:
                # find where number should go
                for j in range(1, i):
                    if array[i] <= array[j] and array[i] >= array[j-1]:
                        # move number to the right spot
                        array[:i+1] = array[:j] + [array[i]] + array[j:i]
                        break
    return array



numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

print(numbers)
insertionSort(numbers)
print(numbers)
