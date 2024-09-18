class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Circular_singly_list:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, new_node):
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            return 
        current_node = self.head
        new_node.next = current_node
        
        while current_node.next is not self.head:
            current_node = current_node.next
        current_node.next = new_node
        self.head = new_node    
     
    def insert_at_end(self, new_node):
        if self.head is None:
            print('list is empty to display')
        current_node = self.head
        while current_node.next is not self.head:
            current_node = current_node.next
        current_node.next = new_node
        new_node.next = self.head

    def insert_node_between(self, new_node, position):
        pass
        if self.head is None:
            self.insert_at_beginning(new_node)
            return
        i =1
        prev_node = None
        current_node = self.head
        if position == 1:
            self.insert_at_beginning(new_node)
            return 
        while i < position :
        # and current_node.next is not self.head:
            prev_node = current_node
            current_node = current_node.next 
            i+=1
        # if current_node.next is self.head:
        #     self.insert_at_end(new_node)
        #     return
        prev_node.next = new_node
        new_node.next = current_node    
    
    def delete_at_beginning(self):
        if self.head is None:
            print('there is noting to delete:')
            return
        temp_self_node = self.head
        self.head = temp_self_node.next 
        current_node = self.head 
        while current_node.next is not temp_self_node:
            current_node = current_node.next 
        current_node.next = self.head
        del temp_self_node
        
    def delete_at_end(self):
        if self.head is None:
            print('there is nothing to delete')
            return
        current_node = self.head
        prev_node = None
        while current_node.next is not self.head:
             prev_node = current_node      
             current_node = current_node.next
        prev_node.next = self.head
        del current_node     
    
    def delete_at_position(self, position):
        pass
        if self.head is None:
            print('cant perform delete as list is empty')
            return
        if position == 1:
            self.delete_at_beginning()
            return
        i = 1
        current_node = self.head
        while i < position-1:
            current_node = current_node.next
            i+=1
        to_delete_node = current_node.next 
        current_node.next = to_delete_node.next
        del to_delete_node
    
    def exchange_first_last_nodes(self):
        pass
        if self.head is None or self.head.next is self.head:
            return self.head
        else:
            prev_node = None
            current_node =self.head
            while current_node.next is not self.head:
                prev_node = current_node
                current_node = current_node.next
            
            current_node.next = self.head.next # d-b  || a-b-c-d ===> d-b-c-a
            self.head.next = current_node # a-d
            prev_node.next = self.head
            self.head = current_node 

    def is_circular(self):
        if self.head is None:
            return 0
        else:
            current_node = self.head
            while current_node.next is not self.head:
                current_node = current_node.next
            if current_node.next is self.head:
                return 1
            else:
                return 0
        

    def display(self):
        if self.head is None:
            print('list is empty to display')
            return
        current_node = self.head
        while current_node.next is not self.head:
            print(current_node.data, current_node.next.data)
            current_node = current_node.next 
        print(current_node.data, current_node.next.data)

node1 = Node('c')
node2 = Node('b')
node3 = Node('a')
node4 = Node('d')
node5 = Node('e')
clist = Circular_singly_list()
clist.insert_at_beginning(node1)
clist.insert_at_beginning(node2)
clist.insert_at_beginning(node3)
clist.insert_at_end(node4)
clist.insert_node_between(node5,5)

clist.display()

print('*****************************')
# print(clist.is_circular())
# clist.delete_at_end()
# clist.delete_at_position(5)
# clist.delete_at_beginning()
# clist.delete_at_beginning()
clist.exchange_first_last_nodes()

clist.display()
