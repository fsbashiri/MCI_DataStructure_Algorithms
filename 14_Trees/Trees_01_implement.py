class Node():
    def __init__(self, data) -> None:
        self.data = data
        self.right = None
        self.left = None
        pass

    def __str__(self) -> str:
        return str(self.__dict__)

    def __repr__(self) -> str:
        return f"Node({self.data})"


class BinarySearchTree():
    def __init__(self) -> None:
        self.root = None
        pass

    def __str__(self) -> str:
        # return str(self.__dict__)
        return str(traverse(self.root))

    def insert(self, value):
        newNode = Node(value)
        # if the tree is empty
        if self.root is None:
            self.root = newNode
            return self
        # if the tree is not empty
        currNode = self.root
        while True:
            if value < currNode.data:
                if currNode.left is None:
                    currNode.left = newNode
                    return self
                currNode = currNode.left
            else:
                if currNode.right is None:
                    currNode.right = newNode
                    return self
                currNode = currNode.right

    def lookup(self, value):
        # if the tree is empty
        if self.root is None:
            return False
        # if the tree is not empty
        currNode = self.root
        while currNode is not None:
            if value < currNode.data:
                if currNode.left is None:
                    return False
                currNode = currNode.left
            elif value > currNode.data:
                if currNode.right is None:
                    return False
                currNode = currNode.right
            else:
                return currNode
    
    def remove(self, value):
        # if the tree is empty
        if self.root is None:
            return False
        # if the tree is not empty
        currNode = self.root
        parentNode = None
        while currNode is not None:
            if value < currNode.data:
                # walk to the left
                parentNode = currNode
                currNode = currNode.left
            elif value > currNode.data:
                # walk to the right
                parentNode = currNode
                currNode = currNode.right
            else:
                # we found the node to remove
                # Case 1: the node has no right child
                if currNode.right is None:
                    if parentNode is None:
                        self.root = currNode.left
                    else:
                        # if parent > current, make current left child a child of parent
                        if currNode.data < parentNode.data:
                            parentNode.left = currNode.left
                        # if parent < current, make left child a right child of parent
                        elif currNode.data > parentNode.data:
                            parentNode.right = currNode.left
                # Case 2: the node has a right child that does not have a left child
                elif currNode.right.left is None:
                    if parentNode is None:
                        self.root = currNode.left
                    else:
                        currNode.right.left = currNode.left
                        # if parent > current, make right child of the left the parent
                        if currNode.data < parentNode.data:
                            parentNode.left = currNode.right
                        # if parent < current, make right child a right child of the parent
                        elif currNode.data > parentNode.data:
                            parentNode.right = currNode.right
                # Case 3: the node has a right child that has a left child
                else:
                    # find the right child's left most child
                    leftmost = currNode.right.left
                    leftmostParent = currNode.right
                    while leftmost.left is not None:
                        leftmostParent = leftmost
                        leftmost = leftmost.left
                    # Parent's left subtree is now leftmost's right subtree
                    leftmostParent.left = leftmost.right
                    leftmost.left = currNode.left
                    leftmost.right = currNode.right
                    if parentNode is None:
                        self.root = leftmost
                    else:
                        if currNode.data < parentNode.data:
                            parentNode.left = leftmost
                        elif currNode.data > parentNode.data:
                            parentNode.right = leftmost

                return True
        return False
                        
                
                

def traverse(node):
    tree = {
        'value': node.data,
        'left': None,
        'right': None
    }
    if node.left is not None:
        tree['left'] = traverse(node.left)
    if node.right is not None:
        tree['right'] = traverse(node.right)
    return tree



tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)
tree.remove(20)
print(tree.lookup(20))
print(traverse(tree.root))

  #     9
  #   4   20
  # 1  6 15  170

