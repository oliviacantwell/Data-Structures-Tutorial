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
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def remove_head(self):
        self.head.next.prev = None
        self.head = self.head.next
    
    
    
    def remove_tail(self):
    # Add your code here
        self.tail.prev.next = None
        self.tail = self.tail.prev

    def insert_tail(self,data):
    # Add your code here
        new_node = Node(data)
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node


# Use this code to test it
    def printList(self):
        curr = self.head
        print("Start")
        while curr is not None: 
            print(curr.data)
            curr = curr.next
        print("End")

x = LinkedList() #lets first fill up a list
x.insert_head(3)
x.insert_head(5)
x.insert_head(9)
x.insert_head(0)
x.printList() # 0, 9, 5, 3
x.remove_head()
x.printList() # 9, 5, 3

# Now let's test your code!
x.insert_tail(6)
x.insert_tail(7)
x.printList() # 9, 5, 3, 6, 7
x.remove_tail()
x.printList() # 9, 5, 3, 6