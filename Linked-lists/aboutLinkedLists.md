# Linked Lists
## Introduction
A linked list is a useful way to dynamically allocate memory unpon runtime. In other words, when you use an array, you must allocate beforehand how much memory you will be using. A linked list, on the otherhand, can have memory added while the program is running. 
<br>
There are two types of linked lists: regular linked lists and doubly-linked lists. We will be covering both in our explanation section, but only doubly-linked lists in the code example and practice problem. 

## Explanation
### Regular Linked List
Unlike a dynamic array, a linked list's pieces of data are not store next to each other. They are stored randomly within memory. Because of this, we need to know where the next peice of data is when looking through the list. Each node (or piece of data) has a pointer to where the next piece of data is located. The very first node is known as the head. Think of it as the engine of the train. When you're in a traincar, you don't know how far from the front you are or where you are at all in the line. But if you're in the engine room, then you know where you are; you're at the front! 

<br>
<br>

![](linked1.png)
<br>
<br>
<br>

### Doubly-Linked List
A doubly-linked list has all the qualities of a regular list plus more. A regular linked list has an address to the next node, so you can go from one node to the next. But what happens if you want to go backwards in the list? Where's the previous node? It doesn't know! There's no pointer to direct it. This is where doubly-linked lists come in handy. You can put a second address in the node to the location of the previous node. To recap, each node has the data inside of it (such as number(s), letter(s), etc), it has a pointer to the location of memory of the previous node, and it has a pointer to the location of memory of the next node. The very first node is the head. Additionally for a doubly-linked list, the very last node is the tail. 
<br>
<br>

![](linked2.png)
## Performance

## Code Example
Now that we know what a linked list is, how do we use it? How do we insert and delete nodes? 


```python
"""
The Set Up
"""
# first we have to create a class the nodes
class Node: 
    def _init_(self, data):  # initialize nodes
        self.data = data #node will have data in it
        self.next = None #node will have next link
        self.prev = None #and a prev link

# next we create a class for the list
class LinkedList:
    def _init_(self): #initialize list
        self.head = None #create the head node
        self.tail = None #create the tail node

"""
How to insert a head
"""
    def insert_head(self, value):
    # First, create a new node
        new_node = LinkedList.Node(value)
    # Second, set the pointer to the next node (we will call this the "next") to the what the head currently is
        new_node.next = self.head
    # Third, set the "prev" (the pointer that is pointing to the previous node) of the old head to the new head
        self.head.prev = new_node
    # Last, set the new node as the head
        self.head = new_node

"""
How to remove the head
"""
    def remove_head(self):
    # First, delete the "previous" link from the second node to the head
        self.head.next.prev = None
    # Second, set title of head to the second node
        self.head = self.head.next

"""
How the insert a node into the middle
Note: whenever we insert a node, we have to be currently in a node, typically the node before the spot where we want to put the new node. In other words, we will do everything from the perspective of the "current" node.
"""
    def insert(self, value):
    # First, create a new node
        new_node = LinkeList.Node(value)
    # Second, set the "previous" of the new node to the node we are in
        new_node.prev = curr
    # Third, set the "next" of the new node to the node right after the current node, or what will be after the new node
        new_node.next = curr.next
    # Fourth, set the "previous" of the node after the current node to the new node
        curr.next.prev = new_node
    # Fifth, set the "next" of the current to the new node
        curr.next = new_node

"""
How to delete a node from the middle
Note: we will delete the "current" node 
"""
    def delete(self):
    # First, set the "previous" of the next node to the node before the node being deleted
        curr.next.prev = curr.prev
    # Second, set the "next" of the node before the current to the next node after current
        curr.prev.next = curr.next
```

## Practice 
You may have noticed I left a few instructions out... How do you delete and insert the tail? Well lets see if you can figure it out! Copy the code below to get setup.

```python
class Node: 
    def __init__(self, data):  # initialize nodes
        self.data = data #node will have data in it
        self.next = None #node will have next link
        self.prev = None #and a prev link

class LinkedList:
    def __init__(self): #initialize list
        self.head = None #create the head node
        self.tail = None #create the tail node


    def insert_head(self, data):
        new_node = Node(data)
        
        if self.head is None: #if the list is empty, make the head the tail as well
            self.head = new_node
            self.tail - new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def remove_head(self):
        self.head.next.prev = None
        self.head = self.head.next
    
    
    def remove_tail(self):
    # Add your code here

    def insert_tail(self,data):
    # Add your code here


    def printList(self): # Use this to print out your list
        curr = self.head
        print("Start")
        while curr is not None: 
            print(curr.data)
            curr = curr.next
        print("End")

# Use this code to test it
x = LinkedList() #lets first fill up a list
x.insert_head(3)
x.insert_head(5)
x.insert_head(9)
x.insert_head(0)
printList() # 0, 9, 5, 3
x.remove_head()
printList() # 9, 5, 3

# Now let's test your code!
x.insert_tail(6)
x.insert_tail(7)
printList() # 9, 5, 3, 6, 7
x.remove_tail()
printList() # 9, 5, 3, 6
```

[Link to Solution](Linked-lists/linkedListSolution.py)