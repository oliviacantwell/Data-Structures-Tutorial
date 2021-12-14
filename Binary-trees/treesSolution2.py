class Tree:
    
    class Node:
        def __init__(self, value):
            self.left = None
            self.right = None
            self.value = value

    def __init__(self):
        self.root = None
        
    def insert(self, value): #This is our starting function
            if self.root is None: # is there even anything in the tree? If there isn't, then our search stops there and the new node is the root
                self.root = Tree.Node(value)
            else: #if there is something in the tree, then call the function that will take us through the branches
                self._insert(value, self.root) #pass in the root so we know to start there
        
    def _insert(self, value, node):
            if value < node.value: #if the value of the new node (11) is less than the node we are comparing it to, then go left
                if node.left is None: #if there is no other node
                    node.left = Tree.Node(value) #then we place it here!
                
                else: #if there is another node...
                    self._insert(value, node.left) #call the function again, but start off on the left node now
            
            elif value >= node.value: # if the new node is more than or equal to the node we are comparing it to
                if node.right is None: #if there is no other node
                    node.right = Tree.Node(value) #then we place it here!

                else: #if there is another node...
                    self._insert(value, node.right) #call the function again, but start off on the right node now

    
    def __iter__(self): #starting function that starts recursion
        yield from self._inOrder(self.root) #start at the root
    
    def _inOrder(self, node): 
        if node is not None: # base case: make sure there is something there! Otherwise stop
        
            yield from (self._inOrder(node.left)) #first go down left side
            yield (node.value) # next get the value
            yield from (self._inOrder(node.right)) #then go on the right


tree = Tree()
tree.insert(8)
tree.insert(2)
tree.insert(1)
tree.insert(9)
tree.insert(13)
tree.insert(4)
tree.insert(7)
tree.insert(3)

# x.inOrder()
for i in tree:
    print(i)


# Your tree should look like this
#             8
#           /   \
#          2     9
#         / \   / \
#       1    4     13
#           / \
#          3   7
#
# the max height is 4 (from 7 or 3 to 8)