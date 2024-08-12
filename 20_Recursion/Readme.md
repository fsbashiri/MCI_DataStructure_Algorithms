# Introduction

Recursion isn't technically an algorithm, but more of a concept. Recursion is when you define something in terms of itself; a function that refers to itself inside of the function. 

Recursion is really good for tasks that have repeated subtasks to do. This concept is used in searching and sorting algorithms, such as traversing a tree.

# Base case

One of the biggest problems with recursion is that it can cause stack overflow; adding to the call stack but nothing popping out. A way out of this issue, is using a **base case** or a **stop point**.

Recursive functions have two paths. One is the recursive path that calls the function again and runs it. The other is the base case that stops calling the function.

`counter = 0`
`def inception(counter):`
    `if counter > 3:`
        `return 'done'`
    `counter += 1`
    `print(counter)`
    `return inception(counter)`
`print(inception(counter))`

There are three steps to take:
1. Identify the base case: the if statement in the example above
2. Identify the recursive case: calling inception within inception
3. Get closer and closer and return when needed. Usually you have 2 returns: for the base case and the recursive case

## Recursive vs. Iterative

**Remember**: anything you do with a recursion CAN be done iteratively (loop)

Recursion:
- Pros: Dry code and readability
- Cons: Large stack

New rule: every time you are using a tree or converting something into a tree, consider recursion.
1. divided into a number of subproblems that are smaller instances of the same problem.
2. Each instance of the subproblem is identical in nature.
3. The solutions of each subproblem can be combined to solve the problem at hand.

You will see lots of divide and conquer using recursion! 

Some topics that recursion is useful for:
- Merge sort
- Quick sort
- Tree traversal
- Graph traversal

# Python codes

- introduction to recursion and base case: [Rec_01_intro.py](./Rec_01_intro.py)
- Exercise Factorial: [Rec_02_Factorial.py](./Rec_02_Factorial.py)
- Exercise Fibonacci: [Rec_03_Fibonacci.py](./Rec_03_Fibonacci.py)
- Exercise reverse string: [Rec_04_reverseString.py](./Rec_04_reverseString.py)
- Exercise number of islands: [Rec_05_countIslands.py](./Rec_05_countIslands.py)

