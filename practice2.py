class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
    
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_begining(self, node):
        if self.head is None:
            self.head = node
            return
        # next_node = self.head
        # self.head = node
        # next_node.prev = node
        # node.next = next_node
        # 88888888888888888888888888888
        # node.next = self.head
        # node = self.head.prev
        # self.head = node
        # 8888888888888888888888888888
        # temp_node = self.head
        # self.head = node
        # node.next = temp_node
        # temp_node.prev = node
        # **********************
        node.next = self.head
        self.head.prev = node
        self.head = node

    def insert_node_between(self,node, position):
        if self.head is None:
            self.insert_at_begining(node)
            return
        if position == 1:
            self.insert_at_begining(node)
            return
        i=1
        current_node = self.head
        while i != position-1:
            current_node = current_node.next
            i+=1
        store_node = current_node.next
        current_node.next = node
        node.next = store_node
        node.prev = current_node
        store_node.prev = node
        # del store_node, current_node, node # to remove these variables from memory

    def insert_at_last(self, to_insert_node):
        pass
        if self.head is None:
            self.insert_at_begining(node)
            return
        
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = to_insert_node
        to_insert_node.prev = node
        to_insert_node.next = None


    def delete_first_node(self):
        if self.head is None:
            print('can\'t perform delete operation')
            return
        node = self.head
        self.head = node.next
        self.head.prev = None
        node.next = None
        del node 

    def delete_last_node(self):
        if self.head is None:
            print('can\'t perform delete operation')
            return 
        node = self.head
        while node.next is not None:
            prev_node = node
            node = node.next
        prev_node.next = None
        node.prev = None
        del node

    def delete_between_node(self, position):
        if self.head is None:
            print('list is empty to delete')
            return
        i=1
        node = self.head
        
        if position == 1:
            self.delete_first_node()
            return
        print('length :', self.list_length())
        length_list = self.list_length()
        print('position , list_length :', position , length_list)
        if position == length_list:
           self.delete_last_node()
           return
        
        while i < position:
            # print('x')
            node = node.next
            i+=1

        prev_node = node.prev
        next_node = node.next 
        prev_node.next = next_node
        next_node.prev = prev_node
        del node 

    def list_length(self):
        if self.head is None:
            return 0
        node = self.head
        i=0
        while node is not None:
            node = node.next
            i+=1
        return i 
     
    def reverse_iteratively(self):
        current_node = self.head
        prev_node= None
        next_node = None
        while current_node is not None:
            # print('not sure')
            # temp_node= current_node
            # prev_node = current_node.prev
            # current_node.prev = current_node.next 
            # current_node.next = prev_node
            # current_node = temp_node.next
            prev_node = current_node.next # to move to current_node to next node for traversing
            next_node = current_node # this is important because it carries the node which needs to be made as head
            current_node.next  = current_node.prev # to change the prev node to next node and next node to prev node address for a current_node
            current_node.prev = prev_node # to change the prev node to next node and next node to prev node address for a current_node
            current_node = prev_node # updating the currrent_node to the next node 
        self.head = next_node

    def reverse_headrecursively(self, current_head):
        if current_head is None or current_head.next is None:
            current_head.next = current_head.prev
            current_head.prev = None
            return current_head
        instance_head = self.reverse_headrecursively( current_head.next)
        temp_prev = current_head.prev 
        current_head.prev = current_head.next
        current_head.next = temp_prev
        
        return instance_head
    

    def display(self):
        if self.head is None:
            print('list is empty to')
            return
        node = self.head
        # print(node, node.next)
        while node is not None:
            print(node.data)
            node = node.next


node1 = Node('a')
node2 = Node('b')
node3 = Node('c')
node4 = Node('d')

list = DoublyLinkedList()
list.insert_at_begining(node3)
list.insert_at_begining(node2)
list.insert_at_begining(node1)
list.insert_node_between(node4,2)

list.display()

# list.delete_between_node(1)
# list.reverse_iteratively()
list.head = list.reverse_headrecursively(list.head)
print('*****************************************************')





list.display()

