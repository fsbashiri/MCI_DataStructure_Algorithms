# Introduction

Arrays have limited memory and poor performance in insert/delete operations where it needs to shift elements. Hash tables solve this issue, but are unordered. 

Linked lists contain **a set of nodes**. Each node has two elements: the **value** of the data, and a **pointer** to the next node. The first node is called the **head**, and the last node is called the **tail**. The last node points to null! Here is an [animated demonstration](https://visualgo.net/en/list?slide=1) of Linked Lists.

Linked lists can be sorted, unsorted, and contain any sort of data type. Some languages do not ship with a built-in linked list.

# Why Linked List?

**Insert/delete**: Linked lists have a sort of loose structure that allows you to insert a value into the middle of the list by simply resetting a few pointers. This is the same for deleting the node. 

**Linked list vs. arrays**: The main difference between arrays and linked lists is that in an array, elements are indexed. In a linked list, you start at the head and traverse the list until you get to the item, which is O(n).

**Traversal**: The idea of traversal is the same as iteration that we did with arrays. Except we like to call this traversal because you don't really know when the linked list will end. You start from the head and you keep going until you hit null -> While loop in implementation.

**Advantage of arrays**: Most computers have caching systems that make reading from sequential memory (e.g., iterating through items like an array) faster than reading scattered addresses (i.e., traversing through a linked list). **However,** these inserts that we can do in the middle of a linked list is a lot better than an array!

**Advantage over hash tables**: The one advantage that linked lists has over hash tables is that there is some sort of order to linked list.

| Operation   | Big-O |
| ----------- | ----- |
| **prepend** | O(1)  |
| **append**  | O(1)  |
| **lookup**  | O(n)  |
| **insert**  | O(n)  |
| **delete**  | O(n)  |

# Pointer

A pointer is a reference to another place in memory, another object or another node. In the code example below, there is only one entry in the RAM. Both `obj1` and `obj2` are a pointer to the same location in memory where `'a' = 1`. By accessing property `a` in `obj1`, both `obj1` and `obj2` changed because we've created a pointer!

```
obj1 = {'a': 1}
obj2 = obj1
obj1['a'] = 'booya'
```

A linked list can be implemented using pointers!

# Singly vs. Doubly Linked Lists

A singly LL only points to the next node. Therefore, we can traverse from head to tail. A doubly LL points to the next and the previous nodes, and allows us to traverse backwards. So, lookup can technically be of O(n/2), which we have a rule to remove constants and so, we say its O(n).

## Pros and Cons

A singly linked list:
- (+) has a fairly simple implementation
- (+) requires lesser memory
- (+) runs less operation and faster, when doing things like delete and insert
- (-) cannot be iterated in reverse (i.e., traverse from back to front)
- (-) can actually be lost in memory forever if we ever lose the reference to the head node of the list.

**So singly list is appropriate to use when** you have less memory or memory is really expensive and you want to be careful of how much you use. And your main goal is that you want to do fast insertion and deletion and you don't really have that much searching, especially when you have insertion at the beginning of a list.

A doubly linked list:
- (+) can be traversed from both directions
- (+) can delete previous node fairly easily
- (-) requires more memory and storage
- (-) requires extra operations to perform

**So doubly link lists are really good when** you don't have that much limitation on memory. And, when you want good operation for searching for elements.

# Summary

**Pros:**
- Fast insertion
- Fast deletion
- Ordered
- Flexible size

**Cons:**
- Slow lookup
- More memory

