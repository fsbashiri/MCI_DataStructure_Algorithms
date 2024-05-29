### Before you start

**GitHub reps**
Andrei's GitHub repo: [**Andrei's GitHub repo specific to this course**](https://github.com/aneagoie/ztm-master-the-coding-interview-ds-algo)

The programming examples in the course is written in JavaScript. The python version of them can be found here:
- [**https://github.com/theja-m/Data-Structures-and-Algorithms**](https://github.com/theja-m/Data-Structures-and-Algorithms)
- [**https://github.com/VicodinAbuser/ZTM-DS-and-Algo-Python**](https://github.com/VicodinAbuser/ZTM-DS-and-Algo-Python)

**Online tools**
- https://replit.com/~
- https://glot.io/

**Cheatsheet**
- Online link: [Big O cheatsheet - ZTM](https://zerotomastery.io/cheatsheets/big-o-cheat-sheet/?utm_source=udemy&utm_medium=coursecontent)
- Online link: [Big O cheatsheet](https://www.bigocheatsheet.com/)
- YouTube link: [Big O Notation Tutorial](https://youtu.be/TUiv2UgDgOQ)
- Cheatsheet file: [PDF](obsidian://open?vault=Obsidian%20Vault&file=Master%20the%20coding%20interview%2FSection%203%20-%20BigO%2FBigO-cheat-sheet.pdf)

### Summary

**What is good good code?**
- Readable
- Memory: space complexity
- Speed: time complexity

**Rule book**
- Rule 1: Always worst Case
		When we think about scalability, we cannot assume things will go well. For example, when looping over an array, the item of interest might be the last index we will check.
- Rule 2: Remove Constants
		In scalability, when *n* gets bigger and bigger, we don't care about adding an extra 100 steps! We care about how the line increases when the number of elements increases. We care it's linear, not how steep (e.g., O(n) vs. O(2n)) it is!
- Rule 3: Different inputs should have different variables. 
	- O(a+b): for steps in order
	- O(a*b): for nested steps
- Rule 4: Drop Non-dominant terms
		With Big-O we are worried about scale and as things get larger and larger!

**Big-O Complexity**

![[BigO_Complexity_Chart.png]]

![[Section_3_BigO/BigO_Complexity_Chart.png]]


**Type of Big Os:**

| Big O           | Type        | Description                                             |
| --------------- | ----------- | ------------------------------------------------------- |
| **O(1)**        | Constant    | no loops                                                |
| **O(log N)**    | Logarithmic | searching algorithms if they are sorted (Binary search) |
| **O(n)**        | Linear      | loops through n times                                   |
| **O(n log(n))** | Log Liniear | usually sorting operations                              |
| **O(n^2)**      | Quadratic   | two nested loops                                        |
| **O(2^n)**      | Exponential | recursive algorithms that solves a problem of size N    |
| **O(n!)**       | Factorial   | adding a loop for every element                         |

Check out this [online cheatsheet](https://www.bigocheatsheet.com/) for the time and space complexity of **common data structure operations** and **array sorting algorithms**. 

