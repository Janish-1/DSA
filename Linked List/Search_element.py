class Node:
    def __init__(self,key):
        self.key = key # Assign data
        self.next = None # Initialize next as null

class LinkedList:
    def __init__(self):
        self.head = None # Initialize head as None

    # Add a new node with key "new_key" at the begining of the linked list
    def push(self,new_key):
        new_node = Node(new_key)
        new_node.next = self.head
        self.head = new_node

# Create a linked list object
llist = LinkedList()

# Add new nodes to the linked list
llist.push(10)
llist.push(30)
llist.push(11)
llist.push(21)
llist.push(14)

# Key to search for in the linked list
x = 21

# Create a temp variable to traverse the linked list
temp = llist.head

# List to store the keys in the linked list
v = []

# Traverse the linked list and store the keys in the list
while(temp):
    v.append(temp.key)
    temp = temp.next 

# Check if 'x' is in the list 'v'
if x in v:
    print("YES")
else:
    print("NO")
