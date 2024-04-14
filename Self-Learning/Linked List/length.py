# Length of a Linked List

# Node class
class Node:
    # Function to initialize node object
    def __init__(self,data):
        self.data = data 
        self.next = None # Initialize next as null
    
class LinkedList:
    def __init__(self):
        self.head = None

    # This function is in LinkedList class.
    # Insert new node at the begining of Linked List.
    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def getCount(self):
        temp = self.head # Initialize temp
        count = 0 # Initialize count

        # Loop while end of linked list is not reached
        while (temp):
            count+=1
            temp = temp.next
        return count
    
if __name__ == '__main__':
    llist = LinkedList()
    llist.push(1)
    llist.push(3)
    llist.push(1)
    llist.push(2)
    
    print("Count of nodes is:",llist.getCount())


    