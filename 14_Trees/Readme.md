# Introduction

Trees are like linked lists. A linked list is a tree that has one path, and is linear. The difference: In a tree, a node can only point to a child (arrows always point down). 

Trees have a hierarchical structure. As opposed to linked lists and arrays, which are linear, trees can have zero or more child nodes. Any child decends from one parent. Parent-Child relationship is unidirectional (i.e., one-way). Within a tree you can have sub-trees. A node in a tree can have any sort of information.

Different types of nodes:
- **Root**: The top most node
- **Parent**: Any node that has a child; a node below
- **Child**: Any node that has a parent; a node on top
- **Leaf**: All very end nodes 
- **Sibling**: Nodes in a same level, with a same parent

In trees, there is one entry point: the root. There are many different types of trees. We will go over the most important and widely used ones. 

# 1. Binary Tree

Two simple rules:
1. Each node can only have 0, 1, or 2 child nodes. 
2. Each child can only have 1 parent! 

Each node represents a certain state. A few terminalogy:
- **Full Binary Tree**: Each node has either 0 or 2 children. 
- **Perfect Binary Tree**: Each node has either 0 or 2 children. Also, the bottom layer of the tree is completely filled, meaning that nothing is missing. => Very desirable tree, because it is really efficient. They have two properties:
	1. The number of total nodes on each level doubles as we move down the tree. Number of nodes: 1 -> 2 -> 4 -> 8
	2. The number of nodes on the last level = the sum of the number of nodes on all the other levels + 1 => meaning that about half of our nodes are on the last level. You can gain efficiency if you can somehow avoid visiting every node.

## 1.1. Big-O

- At each level, start counting from 0, we have `2^n` number of nodes (i.e., Number of nodes: 1 -> 2 -> 4 -> 8).
- Total number of nodes = `2^h - 1` , where `h` is the height of the tree (start counting from 1). 
For example, a tree of `h = 3`, has three levels, with 1, 2, and 4 nodes in each level, and `2^3 - 1 = 8 - 1 = 7` nodes in total. Why height `h = log(N)` is important? The height is the maximum number of decisions that we have to make before we can find out the node that we are interested in. 

| Operation  | Big-O    |
| ---------- | -------- |
| **lookup** | O(log n) |
| **insert** | O(log n) |
| **delete** | O(log n) |
The notation of `O(log n)` is like looking through a phonebook. You don't need to check every name in the phonebook. You can simply do what's called **divide and conquer** by exploring a subset of each section before you find someone's phone number. In another words, the choice of the next element on which to perform some sort of action is one of several possibilities, and only one needs to be chosen. We don't need to check every single element, which makes it efficient and fast. 

## 1.2. Binary Search Tree

A subset of Binary Tree. This data structure is great for comparing things, and in contrast to hash tables, it preserves relationships. In BST, you don't have to iterate through every single item. A tool for visualization is [here](https://visualgo.net/en/bst?slide=1).

Rules: 
1. All child nodes in the tree to the right of the root node must be greater than the current node. That means if I keep going to the right, the number or the value of the node constantly increases.
2. A node can only have up to two children. 

**Balanced vs. Unbalanced:**

A balanced BST has grown on both sides equally. An unbalanced one has grown more on one side, resulted in looking more like a linked list. In that case, the complexity of operations are more like `O(n)`. There are ways to balance a search tree, that are available in most libraries and tools. 

**Performance implications:**

- Pros:
	- Better than O(n)
	- Ordered; if it is balanced
	- Flexible size; we can place the node anywhere in memory 
- Cons:
	- No O(1) operation we have to do some sort of traversal through the tree for any sort of operation

**Auto-balancing trees upon insertion:**

Two popular types of trees that automatically rebalance itself are **AVL Tree** and **Red/Black Tree**. Resources for more information: 
- AVL Tree [Animation](https://www.cs.usfca.edu/~galles/visualization/AVLtree.html) and [how it works](https://medium.com/basecs/the-little-avl-tree-that-could-86a3cae410c7)
- Red/Black Tree [Animation](https://www.cs.usfca.edu/~galles/visualization/RedBlack.html) and [how it works](https://medium.com/basecs/painting-nodes-black-with-red-black-trees-60eacb2be9a5)

# 2. Heap 

When it comes to heap, we're most interested in binary heap, meaning that a node can have two children at most. Every child belongs to a parent that has a higher priority or value. Therefore, in a binary heap, every node on the top level has a greater value than every node on the next level down and a heap can be used in any algorithm where ordering is important.

## 2.1 Big-O

Because a heap tree is not ordered like the binary tree is, for a lookup operation we have to iterate through all nodes. Therefore, a lookup operation has `O(n)` complexity. Time complexity of binary heap data structure:

| Operation  | Big-O    |
| ---------- | -------- |
| **lookup** | O(n)     |
| **insert** | O(log n) |
| **delete** | O(log n) |
Binary heap DS is useful for comparative operations. For example, finding nodes that have a value over 33. When inserting a node, at the best case it takes O(1) and at the worst case it takes O(log n). The worst case happens when it needs to bubble up and switch nodes. 

## 2.2. Priority Queue

Note: memory heap is not the same thing as heap data structure. Similar naming is coincidental. 

Binary heaps take up the least amount of space possible because it's always left to right insertion. So there's no concept of an unbalanced binary heap. They are always a complete binary tree.

Binary heaps are useful for priority queues. Examples: nightclub lineup while accepting VIPs first, an emergency room that prioritizes patients that have the most severe symptoms

**Performance implications:**

- Pros:
	- Better than O(n)
	- Priority
	- Flexible size; we can place the node anywhere in memory 
	- Fast insert
- Cons:
	- Slow lookup; however, finding the max or the min is fast with O(1).

# 3. Trie

A specialized tree used in searching, most often with text. In most cases, it can outperform other data structures depending on the type of search. Tries allow you to know if a word or part of a word exists in a body of text.

A trie has an empty root, and then letters are added. It is not a binary tree, so it can have as many children as alphabet letters. Another name for trie is **prefix tree**. Examples: auto completion, IP routing, words in a dictionary.

Benefits of trie are speed and space!
- When looking for a word, you need to find the length of the word: O(length)
- Because of the prefixes, you save space. You don't have to store a word not in use.