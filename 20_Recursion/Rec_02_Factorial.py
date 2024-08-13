# Write two functions that finds the factorial of any number. One should use recursive, the other should just use a for loop

def findFactorialRecursive(number):
    # code here
    print(number)
    if number == 1:
        return 1
    return number * findFactorialRecursive(number - 1)
    
    # return answer

def findFactorialIterative(number):
    # code here
    print('\n Iterative')
    answer = 1
    for i in range(2, number+1):
        answer = answer * i
    return answer

print(findFactorialRecursive(3))
print(findFactorialIterative(3))
