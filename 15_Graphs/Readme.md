# Introduction

Graphs are one of the most used data structures in computer science. In short, a graph is simply a set of values that are related in a pairwise fashion. And, it looks like a little network.

Graphs have nodes and edges, and can be in different shapes. Linked lists are a type of trees, and trees are a type of graph. There are certain characteristics that allow us to describe graphs. 
- **Directed vs. Undirected**: facebook uses an undirected graph, and twitter uses a directed graph.
- **Weighted vs. Unweighted**: nodes can carry any type of information, but you can have information in the edges too. 
- **Cyclic vs. Acyclic**: if even in a portion of a graph you can move between nodes and get back to the original node, that graph is cyclic. Otherwise, it's acyclic.

A popular type of graph: **DAG** = **Directed Acyclic Graph**

# Implement a graph

Three ways to build a graph with data structures we've studied so far:
- **Edge list**: A list of edges, where each item in the list shows the nodes on both sides of an edge. For example: `[[0, 2], [2, 3], [2, 1], [1, 3]]`
- **Adjacent list**: A list of adjacencies. The index of each item in the list shows the node number, and the item is a list of nodes that it's connected to. For example: `[[2], [2, 3], [0, 1, 3], [1, 2]]`
- **Adjacent matrix**: A matrix that shows the connected nodes with 0 (no connection), 1 (a connection), or `Wij` (weight of a connection). For example, the above graph can be represented this way:
```[[0, 0, 1, 0],
    [0, 0, 1, 1],
    [1, 1, 0, 1],
    [0, 1, 1, 0]]
```

# Summary

There are many types of graphs, and it gets complicated to talk about Big-O of graphs. Here are pros and cons of graphs:

**Pros**: 
- Useful when it comes to relationships! They are indispensable, as some data needs to be in a graph form.
**Cons**:
- Scaling is hard

# Python codes

- Implementation of an undirected, unweighted graph: [Graph_01_implement.py](./Graph_01_implement.py)


