# Time complexit: O(n^2)
# The number of iterations in this implementation is n*(n-1)/2. 
def bubbleSort(array):
    # Code here
    run = True
    arrLen = len(array)
    while run and arrLen > 1:
        run = False  # if no swap, the array is sorted. Don't run the next loop
        for i in range(arrLen - 1):
            if array[i] > array[i+1]:
                # swap numbers
                array[i], array[i+1] = array[i+1], array[i]
                run = True
        arrLen -= 1 # we don't need to check the last element
    return array

numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

print(numbers)
bubbleSort(numbers)
print(numbers)
