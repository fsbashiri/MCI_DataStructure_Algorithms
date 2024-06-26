# Introduction

**Arrays (i.e., lists)** organizes items sequentially - one after the other in the memory. They are the simplest, probably most widely used, and have the least amount of rules.

| Operation  | Big-O |
| ---------- | ----- |
| **Lookup** | O(1)  |
| **Push** * | O(1)  |
| **Insert** | O(n)  |
| **Delete** | O(n)  |
\* can be of O(n)
# Static vs. Dynamic

There are two types of arrays:
- Static: fixed in size -> create an array of size 8; if you decide to add a new item, you have to copy the entire array, allocate a new block of memory, and paste the entire array into a new location
- Dynamic: copy and re-built an array in a new location

**Important**: Python and Java work based on dynamic arrays. They automatically allocate memory according to the increase in size of the array

In low-level languages like C++ that are based on static arrays, things run faster. Coding in high-level languages with dynamic arrays is easier.

# Example codes

**Introduction** to `O()` of basic operations on arrays: [Array_01_intro.py](./Array_01_intro.py)

**Implementing** a class of arrays: [Array_02_implementing.py](Array_02_implementing.py)

**Reverse a string** by converting it to a list, reversing, and joining back to a string: [Array_03_reverseAString.py](Array_03_reverseAString.py)

**Merging sorted arrays**: [Array_04_mergeSortedArrays.py](Array_04_mergeSortedArrays.py)

More examples on leetcode:
- [Two Sum](https://leetcode.com/problems/two-sum/description/)
- [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/description/)
- [Move Zeros](https://leetcode.com/problems/move-zeroes/description/)
- [Contains Duplicates](https://leetcode.com/problems/contains-duplicate/description/)
- [Rotate Arrays](https://leetcode.com/problems/rotate-array/description/)

# Final note

Pros and cons of Arrays:

**Pros**: 
- Fast lookups
- Fast push/pops
- Ordered

**Cons**:
- Slow inserts
- Slow deletes
- Fixed size (if using static array)
