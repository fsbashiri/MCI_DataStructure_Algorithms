# Introduction

Hash tables or objects are a must, and you'll use them in any coding interview. In Python, the built-in hash table is the **dictionary**.

We get to set a **key** and **value**. The key is used as the index of where to find the value in memory. For example: `basket["grapes"] = 10,000`. A black-box function receives the `key: "grapes"`, and returns what location in the memory to look for the `value: 10,000`.

# Hash functions

A hash function is simply a function that generates a value of fixed length for each input that it gets.

- examples: MD5, SHA-1, SHA-256
- features:
	- One way: you cannot find the key from the gibberish output of the function
	- Indempodent: for the same input, the output is always the same. 
	- Case-sensitive

Hash function can slow things down. For every add/retrieve a property, the key is sent into the hash function to get the memory location. For that reason, hash functions are implemented with an optimum hashing function that exists -> We usually assume a time complexity of `O(1)`

# Collision

Hash tables are fast, because they are not ordered and do not need to be pushed, etc.

| Operation  | Big-O |
| ---------- | ----- |
| **insert** | O(1)  |
| **lookup** | O(1)  |
| **delete** | O(1)  |
| **searc**h | O(1)  |

There are two problems with randomly allocating memory, as we don't have indefinite space! 
1. Unordered keys are not suitable for some applications.
2. Two keys may point to a same location in memory. This is called **collision**. Animated demonstration of collision can be found in this [link](https://www.cs.usfca.edu/~galles/visualization/OpenHash.html).

Collision slows down reading and writing to `O(n/k)` Where K is the size of your hash table. It becomes an operation of `O(n)` because we remove constants. 

Two common ways to deal with collisions:
- Link List (also called separate chaining)
- Other ways such as: Open addressing, Robin Hood hashing

# Python codes

Introduction to hash tables: [hash_01_intro.py](./hash_01_intro.py)

implementation of a hash table: [hash_02_implementation.py](./hash_02_implementation.py)

Exercise: [First Recurring Character](./hash_03_FirstRecurringChar.py)

# Summary

**Pros**:
- Fast lookups; we need a good collision resolution, which is usually been taken care of by the programming language
- Fast inserts
- Flexible keys (depending on the type of hash table)

**Cons**:
- Unordered -> in recent update Python dict has become ordered by default
- Slow key iteration

Hash tables can sometimes improve time complexity with fast access (O(1)), but the tradeoff is increased memory usage!



