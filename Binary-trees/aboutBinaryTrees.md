# Binary Trees
## Introduction
Trees are another basic type of data structure. We will talk about binary trees specifically. Binary trees are an efficient way to sort information that can be easily searched for and found later. Binary trees can be used for 3D games, routers, and search methods. 

## Explanation
Imagine an upside-down plant. That's what a binary tree looks like! The very first node is called the root and the very last nodes or the nodes on the tip of the tree are called the leaves. Each node can point to two nodes. This makes it look like a branch. The node pointing to two other nodes is called the parent node and the nodes beneath or pointed to by the parent node are called child nodes. 
<br>
<br>
<br>
![](binarytree1.PNG)

### Binary Search Tree
Let's talk about a particularly useful type of binary tree: a binary search tree. When we put new information into a binary tree, we can organize our tree so that it is easier to search through and find the information that we want. We start at the root and compare the information value with the value of the root. If the value is greater than the root, we go to the right branch, but if it is less than the root we go to the left branch. Next we compare the value we have with the next node on the branch we went down. Is it greater than or less than? And we choose left or right accordingly until we get to the last node. We insert it as a leaf at the end of the branches. 
<br>
<br>
![](binarytree2.PNG)

Let's say for example we want to insert 11 into our tree. Is it greater than or less than 16? Less than...so we go to the left branch. Is it greater or less than 9? Greater than...so we go to the right. Greater than or less than 12? Less than...so we put it under 12 on the left side. 
### Height
Real fast, let's talk about height. The height is how many nodes are in a branch. For example, if we were to calculate the height of from 13 to 9 in the picture above. The height would be 3 (13, 12, 9). What is the height from 9 to 16? Two (9, 16). The height is important to know if we want to have a balanced binary search tree, but we won't talk about those in this tutorial. 
### Recursion
Now there is one more important topic to run over before we look at some code. To look through binary trees, we use recursion. Recursion is when you call the function inside of itself to re-run through the function. For example:
```python
def hi()
    print("hi!")
    hi()
    pass
```
This function would run forever! It would infinitely print out hi. So we have to have a base case, or a condition that will make it stop. This could be a counter 

```python
def start()
    count = 0
    hi(count)
    pass

def hi()
    count += 1
    if count < 5    
        print("hi!")
        hi(count)
    else
        print("bye")
    pass
```
The base case is when the count value gets up to 5, then the recursion will stop. Notice how we cannot initialize count in the hi() because then count would always equal zero! Thus, we have to initialize it elsewhere and call the hi() function first in the start() function. 
<br>





## Code Example
Let's see what our picture example would look like if we coded it out. First, we need to set things up:
```python
class Tree: # first we make a class within a class. The first represents the tree and the second represents the nodes
        
    class Node:
#lets walk through the branches to see where we should insert
        def __init__(self, value): #set everything up...
            self.left = None
            self.right = None
            self.value = value

    def __init__(self):
        self.root = None

    def insert(self, value): #This is our starting function
        if self.root is None: # anything in the tree? 
#If there isn't, then our search stops there and the new node is the root
            self.root = Tree.Node(value)
        else: 
#if there's something in the tree, call the function that will take us through the branches
            
            self._insert(value, self.root) #pass in the root so we know to start there
    
    def _insert(self, value, node):
        if value < node.value: 
#if the value of the new node  is less than the node we are comparing it to, then go left
            if node.left is None: #if there is no other node
                node.left = Tree.Node(value) #then place here!
            
            else: #if there is another node...
                self._insert(value, node.left) #call the function again, but start off on the left node now
        
        elif value >= node.value: 
# if the new node is more than or equal to the node we are comparing it to
            if node.right is None: #if there is no other node
                node.right = Tree.Node(value) #then place here

            else: #if there is another node...
                self._insert(value, node.right) 
#call the function again, but start off on the right node now
```

So lets summarize the step. We first start at the root. Then we ask if the the root even exists. If it doesn't, then the node we are trying to insert obviously goes there and becomes the root! If the root does exist, then we check to see if it is less than or more than the node. If it is less than, it goes on the left. If it is more than, it goes on the right. Then it recursively calls the function again so we can restep through the process. The base case, or when we stop restepping through the process, is when we find a place where there are no more nodes. That's where we place our new node!
<br>
<br>
Now that we have our tree, how can we step through it to find a value that we are looking for? There are three ways to look through a tree: inorder (left, root, right), preorder (root, left, right), and postorder/backwards (left, right, root). Let's learn about inorder. 

```python

    def __iter__(self): #starting function that starts recursion
        yield from self._inOrder(self.root) #start at the root
    
    def _inOrder(self, node): 
        if node is None: # base case: make sure there is something there! Otherwise stop
            return
        else:
            yield from self._inOrder(node.left) #first go down left side
            yield node.value # next get the value
            yield from self._inOrder(node.right) #then go on the right


    '''
    Next is preorder
    '''
    def __iter__(self):
        yield from self._preOrder(self.root)
    
    def _preOrder(self, node):
        if node is None:
            return
        
        else:
            yield node.value
            yield from self._preOrder(node.left)
            yield from self._preOrder(node.right)

    '''
    Last is postorder
    '''
    def __iter__(self):
        yield from self._postOrder(self.root)
    
    def _postOrder(self):
        yield from self._postOrder(node.left)
        yield from self._postOrder(node.right)
        yield node.value

```
## Note! 
In order to use the __iter__ function (which turns the values into a string that can be looped through and displayed), it is recommended that you only use the function once. Therefore, you should only use the one of the traversing functions at a time. The others should be commented out. 

```python
# to print out the tree, create a for loop that loops through the object
```
<br>
## Performance 
Binary trees are one of the most efficient ways of inserting information. This is because it splits the numbers in half according to their value. Recall that this is exactly what O(log n) does. It splits the numbers in half, looks to see if the node you are inserting is higher or lower than the node you are looking at (in "tree" words, do we go left or right?) and does that repeatedly until it finds the right empty spot.

| Operation | Performance |
| --------- | ----------- |
| insert(value)    | O(log n)        |
| inOrder     | O(n)        |
| postOrder    | O(n)        |
| preOrder     | O(n)        |
| height(node) | O(n)|

## Practice
Let's test your knowledge! I will give you a list of numbers and you must predict what the tree will look like. Use the code you learned above to read out the numbers to double check your work. You may use preorder, inorder, or postorder just as long as the output matches your predication. Bonus points if you can create a function that calculates the max height of the tree for you. 

### Problem 1: 
[4, 9, 10, 3, 6] (you will need to use the insert function to add these into the tree)



### Problem 2:
[8, 2, 1, 9, 13, 4, 7, 3]
<br>
### What does the tree look like, and what is the longest height from a leaf back to the root?
<br>
<br> 

[Solution 1](treesSolution1.py)

[Solution 2](treesSolution2.py)
