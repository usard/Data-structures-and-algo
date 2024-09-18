class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class CircularDoublyLinkedlist:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, new_node):
        pass
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            return
        current_node = self.head
        current_node.prev = new_node
        new_node.next = current_node
        while current_node.next is not self.head:
            current_node = current_node.next
        current_node.next = new_node
        self.head = new_node
        new_node.prev = current_node

    def insert_at_end(self, new_node):
        if self.head is None:
            self.insert_at_beginning(new_node)
            return
        current_node = self.head
        while current_node.next is not self.head:
            current_node = current_node.next
        current_node.next = new_node
        new_node.prev = current_node
        new_node.next = self.head    
    
    def insert_at_between(self, new_node, position):
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
            return
        current_node= self.head
        if position == 1:
            self.insert_at_beginning(new_node)
            return
        i = 1
        while i < position-1:
            current_node = current_node.next
            i+=1
        was_next_node = current_node.next
        current_node.next = new_node
        new_node.prev= current_node
        new_node.next = was_next_node
        was_next_node.prev = new_node
    
    def delete_at_beginning(self):
        pass
        if self.head is None:
            print('no list data to display')
            return
        to_delete_node = self.head
        current_node = self.head
        while current_node.next is not self.head:
            current_node = current_node.next
        current_node.next = to_delete_node.next
        self.head = to_delete_node.next
        self.head.prev = current_node
        
    def delete_at_end(self):
        if self.head is None:
            print('there is nothing to delete ')
            return
        current_node = self.head
        while current_node.next is not self.head:
            current_node = current_node.next
        current_node.prev.next = self.head
        self.head.prev = current_node.prev
        del current_node       
    
    def delete_at_between(self, position):
        pass
        if self.head is None:
            print('list is empty to delete')
            return
        current_node = self.head
        i=1
        if i ==1 :
            self.delete_at_beginning()
            return
        while i < position-1:
            current_node = current_node.next
            i+=1
        to_delete_node = current_node.next
        current_node.next = to_delete_node.next
        to_delete_node.next.prev = current_node
        del to_delete_node
        

    def display(self):
        if self.head is None:
            print('nothing to display')
        current_node = self.head
        while current_node.next is not self.head:
            print( current_node.prev.data,'--->' ,current_node.data,'--->' ,current_node.next.data)
            current_node = current_node.next
        print(current_node.prev.data,'--->' ,current_node.data,'--->' ,current_node.next.data)


node1 = Node('a')
node2 = Node('b')
node3 = Node('c')
node4 = Node('d')
node5 = Node('e')
node6 = Node('f')


clist = CircularDoublyLinkedlist()
clist.insert_at_beginning(node4)
clist.insert_at_beginning(node3)
clist.insert_at_beginning(node2)
clist.insert_at_beginning(node1)
clist.insert_at_end(node5)
clist.insert_at_between(node6,5)

clist.delete_at_beginning()
clist.delete_at_end()
clist.delete_at_between(2)
clist.display()