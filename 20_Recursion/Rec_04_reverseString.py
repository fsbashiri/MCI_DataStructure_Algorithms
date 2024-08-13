# Reverse string iteratively and with recursion

# method 1: iterative
def reverseString(str):
    if len(str) == 0:
        return str
    else:
        result = str[-1]
        for i in range(len(str)-2, -1, -1):
            result += str[i]
    return result

print(reverseString("yoyo master"))

# method 2: recursive with string
def reverseStringRecursive(str):
    if str is None or len(str) < 2:
        return str
    return reverseStringRecursive(str[1:]) + str[0]

print(reverseStringRecursive("yoyo master"))

# method 3: recursive with list
def reverseStringRecursive2(str):
    arrStr = list(str)
    reversedString = []
    def myFunc(arr):
        if len(arr) == 0:
            return
        reversedString.append(arr.pop())
        myFunc(arr)
        return reversedString
    myFunc(arrStr)
    result = "".join(reversedString)
    return result

print(reverseStringRecursive2("yoyo master"))

