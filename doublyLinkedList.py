class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev  = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self,node):
        if self.head is None:
            self.head = node
            # self.next = None
            # self.prev = None
        else:
            # node.next = self.head
            # node.prev = None
            temp_node = self.head
            self.head = node
            node.next = temp_node
            temp_node.prev = node

    def insert_at_end(self, node):
        if self.head is None:
            self.insert_at_beginning(node)
        else:
            current_node = self.head
            while current_node.next is not None:
                  current_node = current_node.next
            current_node.next = node
            node.prev = current_node      
    
    def insert_in_between(self, position):
        pass

    def display(self):
        if self.head is None:
            print('empty list')
            return
        else:
            current_node = self.head
            while current_node is not None:
                print(current_node.data)
                current_node = current_node.next
                
firstNode  = Node(11)
secondNode = Node(22)
thirdNode = Node(33)
fourthNode = Node(44)
fifthNode = Node(55)
sixthNode = Node(66)
seventhNode = Node(77)
eighthNode = Node(88)
dlinkedList = LinkedList()

dlinkedList.insert_at_beginning(firstNode)
dlinkedList.insert_at_beginning(secondNode)
dlinkedList.insert_at_beginning(thirdNode)
dlinkedList.insert_at_beginning(fourthNode)
dlinkedList.insert_at_beginning(fifthNode)
dlinkedList.insert_at_beginning(sixthNode)
dlinkedList.insert_at_end(seventhNode)
dlinkedList.insert_in_between(eighthNode, 2)
dlinkedList.display()