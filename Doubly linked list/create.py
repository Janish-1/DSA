class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

one = Node(3)
two = Node(5)
three = Node(9)

one.next = two
two.next = three
three.next = one