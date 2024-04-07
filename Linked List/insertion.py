# Node class
class Node:
    # Initialize node object
    def __init__(self,data):
        self.data = data # Assign Data
        self.next = None # Initialize next as null 

# Linked List class
class LinkedList:
    # Function to initialize the linked list object
    def __init__(self):
        self.head = None

    # Function to insert a new node at the begining
    def push(self,new_data):
        # 1 & 2: Allocate the node and Put in the data
        new_node = Node(new_data)
        # 3: Make next of new Node as head
        new_node.next = self.head 
        # 4: Move the head to point to New Node
        self.head = new_node

    # Inserts a new node after the given prev_node.
    def insertAfter(self,prev_node,new_data):
        # 1: Check if the given prev_node exists
        if prev_node is None:
            print("The given previous node must inLinkedList.")
            return 
        # 2: Create new node & 3: Put in the data
        new_node = Node(new_data)
        # 4: Make next of New Node as next of prev_node
        new_node.next = prev_node.next
        # 5: Make next of prev_node as new_node
        prev_node.next = new_node 

    # Appends a new node at the end
    def append(self,new_data):
        # 1: Create a new node
        # 2: Put in the data
        # 3: Set next as None
        new_node = Node(new_data)

        # 4: If linked list is empty, make new node as head
        if self.head is None:
            self.head = new_node 
            return 

        # 5: Else traverse till the last node 
        last = self.head 
        while(last.next):
            last = last.next
        
        # 6: Change the next of last node
        last.next = new_node

    # Utility function to print the linked list
    def printList(self):
        temp = self.head 
        while (temp):
            print(temp.data,end=" ")
            temp = temp.next

if __name__ == '__main__':

    # Start with empty
    llist = LinkedList()

    # Insert 6 So linked list becomes 6-> None
    llist.append(6)

    # Insert 7 
    llist.push(7)

    # Insert 1 
    llist.append(4)

    # Insert 8 
    llist.insertAfter(llist.head.next,8)

    print('Created Linked list is: ')
    llist.printList()