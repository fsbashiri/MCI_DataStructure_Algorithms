# Andrei's solution
def mergeSortedArrays1(arr1, arr2):
    mergedAarray = []

    # check inputs
    if len(arr1) == 0:
        return arr2
    if len(arr2) == 0:
        return arr1

    i, array1Item = 1, arr1[0]
    j, array2Item = 1, arr2[0]
    
    # merge arrays
    while (array1Item) or (array2Item):
        if (array1Item is not None) and ((array2Item is None) or (array1Item < array2Item)):
            mergedAarray.append(array1Item)
            if i < len(arr1):
                array1Item = arr1[i]
                i += 1
            else:
                array1Item = None
        else:
            mergedAarray.append(array2Item)
            if j < len(arr2):
                array2Item = arr2[j]
                j += 1
            else:
                array2Item = None
        
    return mergedAarray

# revised Andrei's solution: using ind and len(arr) instead of undefined values
def mergeSortedArrays2(arr1, arr2):
    sorted_array = []
    ind1, len1 = 0, len(arr1)
    ind2, len2 = 0, len(arr2)
    while ind1 < len1 or ind2 < len2:
        if ind1 >= len1:
            sorted_array.extend(arr2[ind2:])
            ind2 = len2
        elif ind2 >= len2:
            sorted_array.extend(arr1[ind1:])
            ind1 = len1
        elif arr1[ind1] <= arr2[ind2]:
            sorted_array.append(arr1[ind1])
            ind1 += 1
        elif arr2[ind2] < arr1[ind1]:
            sorted_array.append(arr2[ind2])
            ind2 += 1
    return sorted_array

# revised Andrei's solution: appending inf at the end of both arrays
def mergeSortedArrays3(arr1, arr2):
    mergedAarray = []

    # check inputs
    if len(arr1) == 0:
        return arr2
    if len(arr2) == 0:
        return arr1

    # merge arrays
    i, lenArray1 = 0, len(arr1)
    j, lenArray2 = 0, len(arr2)
    arr1.append(float('inf'))
    arr2.append(float('inf'))
    while i < lenArray1 or j < lenArray2:
        # print(arr1[i], arr2[j])
        if arr1[i] < arr2[j]:
            mergedAarray.append(arr1[i])
            i += 1
        else:
            mergedAarray.append(arr2[j])
            j += 1
    return mergedAarray


print(mergeSortedArrays3([0,3,4,31], [3,4,6,30]))