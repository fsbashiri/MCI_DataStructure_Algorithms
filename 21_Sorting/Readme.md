# Introduction

Sorting and searching are two of the biggest computer science problems. As the size of data increases, the use of a proper sorting algorithm becomes more and more important. A few sorting algorithms that is covered in this course:
- Bubble sort
- Insertion sort
- Selection sort
- Merge sort
- Quick sort

One important note is that you have to check the sort algorithm available in the language you use and whether it performs as you expect. The way they are implemented may not return results as you expected. 

[Here](https://www.toptal.com/developers/sorting-algorithms) is little tool to compare some sorting algorithms, and an [AlgoRythmic](https://www.youtube.com/user/AlgoRythmics/videos) dance showing how each algorithm works.

# 1. Bubble Sort

In each iteration of the algorithm, compare every two adjacent items and "bubble up" the larger one. After the first loop, the largest number is moved to the end of the array. Therefore, the algorithm requires `n` iterations, where each iteration involves `(n-1)` comparisons. Consequently, the time complexity of the algorithm is `O(n^2)`.

# 2. Selection Sort

In the `i`-th iteration of the algorithm, search for the index of the minimum value (`j`) from index `i` to `n`. Swap the items at indices `i` and `j` to bring the minimum value to the beginning of the list. In the first iteration, the smallest value is placed at the start of the array, and in the next iteration, the next smallest value is placed in the second position, and so on. Repeat this process until all the elements are sorted.

# 3. Insertion Sort

This algorithm is particularly useful for small datasets or when you know the dataset is nearly sorted. In some cases, it can achieve a time complexity of `O(n)`. The algorithm starts at index 1 and iterates through each element of the array. At iteration `i`, it searches for the correct position for the item at index `i` within the subarray `array[0 : i-1]`. By the time the algorithm reaches iteration `j`, the subarray from index 0 to `j-1` is already sorted, and the algorithm only needs to find the appropriate spot for the current item.

# 4. Merge Sort

Merge sort uses the idea of divide and conquer, rather than a nested for loops. This algorithm has a time complexity of `O(n log n)`. The speed comes at the cost of a space complexity of `O(n)`. This algorithm divides the array by half, like making a tree, until each leaf has one item. Then it finds its way back by merging every two leaves into branches, and then branches into larger pieces, and so on.

## Stable vs. Unstable Algorithms

A sorting algorithm is said to be **stable** if two objects with equal keys appear in the same order in sorted output as they appear in the input array to be sorted. Some sorting algorithms are stable by nature like Insertion sort, Merge Sort, Bubble Sort, etc. And some sorting algorithms are not, like Heap Sort, Quick Sort, etc.

In an **unstable** sort algorithm, `straw` or `spork` may be interchanged, but in a stable one, they stay in the same relative positions (that is, since `straw` appears before `spork` in the input, it also appears before `spork` in the output).

# 5. Quick Sort

Quick sort is also a divide and conquer algorithm with `O(n log n)`. It has a space complexity of `O(log n)`, which is better than merge sort that has a space complexity of `O(n)`. However, quick sort algorithm at the worst case, can have a time complexity of `O(n^2)`, happens if the pivot point is not picked properly, such as when the array is nearly sorted and the smallest or the largest item is chosen as a pivot point. This algorithm works by picking a random item as a pivot point, and then searching through the array to place smaller items to the left of the pivot point, and larger items to the right. Now, the right place for the pivot item is set, and the array is divided into two subarrays that each has to go through the same steps until all items are placed at their right spot. 

# 6. Heap sort

 this algorithm has a time complexity of `O(n log n)` and a space complexity of `O(1)` by sorting in place. It doesn't have the worst case quadratic behavior that quick sort has, and neither the memory usage that merge sort has. But on average, it's slower than quick sort in most cases. Therefore, you might use it if you're really worried about worst case and memory. For more information about heap sort, [here](https://brilliant.org/wiki/heap-sort/) is a good resource.

# 7.  Counting Sort and Radix Sort

These are non-comparison sorting algorithms and can beat merge sort and quick sort. The catch is that they can only work on fixed length integers within a certain range because of the way numbers are stored in the memory.

# Which sort is best?

- **Bubble sort**: it's mostly used for educational purposes and is not very efficient. You're never going to use it! 
- **Selection sort**: Like bubble sort, most likely you won't be using it.
- **Insertion sort**: When there is only a few items and mostly sorted data
- **Merge sort**: if you are worried about the worst case scenarios, you should use merge sort. Because it's best, average, and worst time complexities are the same and is `O(n log n)`. If you want to sort in memory and you're worried about space complexity, merge sort is expensive (space complexity of `O(n)`). However, if you can do an external sorting, merge sort is good. 
- **Quick sort**: it has the same speed as merge sort at best and average cases, but less space complexity. So, it's better than merge sort, and is probably one of the most popular sorting algorithms. One downside is the worst case when the pivot is not picked properly. 
- **Heap sort**: This algorithm doesn't have the worst case quadratic behavior that quick sort has, and neither the memory usage that merge sort has. But on average, it's slower than quick sort in most cases. Therefore, you might use it if you're really worried about worst case and memory. 
- **Counting sort** and **Radix sort**: these are non-comparison sorting algorithms and can beat merge sort and quick sort. The catch is that they can only work on fixed length integers within a certain range because of the way numbers are stored in the memory.

# Python codes

- Implementation of Bubble Sort: [Sort_01_bubble.py](./Sort_01_bubble.py)
- Implementation of Selection Sort: [Sort_02_selection.py](./Sort_02_selection.py)
- Implementation of Insertion Sort: [Sort_03_insertion.py](./Sort_03_insertion.py)
- Implementation of Merge Sort: [Sort_04_merge.py](./Sort_04_merge.py)
- Implementation of Quick Sort: [Sort_05_quick.py](./Sort_05_quick.py)


