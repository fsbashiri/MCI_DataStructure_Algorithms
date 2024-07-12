# Introduction

Stacks and Queues (Qs) are:
- very similar, meaning that they can be implemented in similar ways. The main difference is how items get removed from data structure.
- both linear data structures: traverse data elements sequentially one by one. Meaning that only one data element can be directly reached. 
- mainly used to run commands like push, peek, pop -> exclusively deal with the element at the beginning or the end of the data structure. There's no random access operation.

Why would we want to limit the operations you can do? That's actually a benefit because you can control whoever uses this data structure performs only the right operations that are efficient.

# Stacks

**Last In, First Out - LIFO:** You can think of stacks as plates stacked on top of each other vertically, and you can only touch the top plate. You can't really access anything from the bottom.

Usage examples:
- when functions get called in a programming language
- browser history
- writing a piece of text

# Queues

**First In, First Out - FIFO:** You can think of queues as like an entrance to a roller coaster. The first person that arrives in line gets to go first on the roller coaster. 

Usage examples:
- a waitlist app to buy tickets
- a restaurant app where you check in
- Uber and Lyft
- a printer

# Big-O

| Stacks Ops | Big-O |      | Queues Ops | Big-O |
| ---------- | ----- | ---- | ---------- | ----- |
| lookup     | O(n)  |      | lookup     | O(n)  |
| push       | O(1)  | <--> | enqueue    | O(1)  |
| pop        | O(1)  | <--> | dequeue    | O(1)  |
| peek       | O(1)  |      | peek       | O(1)  |
Peek: looking at the first item that's going to come out! 
- In stacks: the last plate
- In queues: the first person in line

# Thoughts on the implementation

Which data structure should we use for implementing stacks and queues? Arrays, or linked lists?

## Stacks

Stacks can be implemented using arrays or linked lists. They both are going to work fairly well. 
- **Advantage of using arrays**: 
	- **Arrays allow something called cache locality**, which makes them technically faster when accessing its items in memory because they're right next to each other versus a linked list that has them scattered all over memory. 
	- And also **linked lists have extra memory associated with them** because we have to hold on to those pointers.
- **Advantage of using linked lists**:  
	- **Linked lists have more dynamic memory**, and we can keep adding things to the list versus an array where you have either a static array or dynamic array that has certain amount of memory. And as soon as it it's about to reach its limit, it's going to have to double up that memory and create new space for it somewhere in memory.

## Queues

Ideally you want to implement queues with linked lists. Queues have FIFO format. If they were implemented using arrays, once you remove the first item from index-0, you'd need to shift all other items from index-1 to the end of the list, that would be a `O(n)` operation. In linked lists, all we have is a pointer to the head, and all we need to do is change the head pointer to the next item in the list, which is a `O(1)` operation.

# Python codes

- implementation of Stack using linked list: [StkQ_01_implement_stack_using_LL.py](./StkQ_01_implement_stack_using_LL.py)
- implementation of Stack using Array: [StkQ_02_implement_stack_using_Array.py](./StkQ_02_implement_stack_using_Array.py)
- implementation of Queue using linked list: [StkQ_03_implement_queue_using_LL.py](./StkQ_03_implement_queue_using_LL.py)
- Exercise implementing queue using stack: [Ex_Queue_using_Stack.py](./Ex_Queue_using_Stack.py)

# Summary

**Pros:**
- Fast operations
- Fast peek
- Ordered

**Cons:**
- Slow lookup