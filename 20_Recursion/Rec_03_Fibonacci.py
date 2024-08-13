# Given a number N return the index value of the Fibonacci sequence, where the sequence is:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144 ...
# the pattern of the sequence is that each value is the sum of the 2 previous values, that means that for N=5 → 2+3

def fibonacciIterative(n):  # O(n)
    # code here;
    arr = [0, 1]
    for i in range(2, n+1):
        arr.append(arr[i-2] + arr[i-1])
    return arr[n]

def fibonacciRecursive(n):  # O(2^n)
    # code here;
    if n < 2:
        return n
    return fibonacciRecursive(n-1) + fibonacciRecursive(n-2)

# print(fibonacciIterative(43))
print(fibonacciRecursive(43))