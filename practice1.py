import math
class Node :
    def __init__(self, data):
        self.data = data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    
    def insert_at_beginning(self,node):
        if self.head is None:
            self.head = node
            self.next = None
        else:
            temp= self.head
            self.head = node
            node.next = temp
            # print('self :',self)

    def insert_at_end(self,node):
        if self.head is None :
            self.head = node 
            node.next = None
        else:
            pointedNode = self.head
            while pointedNode.next is not None :
                pointedNode = pointedNode.next
            pointedNode.next = node
            node.next = None
    
    def insert_at_specific_position(self, to_insert_node, position):
        if self.head is None:
            self.head = to_insert_node
            to_insert_node.next = None
        else:
            if position == 1 :
                self.insert_at_beginning(to_insert_node)
                return
            i=1
            node = self.head
            while i != position-1:
                node = node.next
                i +=1
            if i == position-1:
                to_insert_node.next = node.next
                node.next = to_insert_node

    def delete_first_node(self):
        if self.head is None:
            print('list is empty, can\'t perform delete')
            return
        node = self.head
        first_node = node.next if node.next is not None else None
        self.head = first_node
        node.next = None
        del node

    def delete_last_node(self):
        if self.head is None:
           print('list is empty, can\'t perform delete')
           return
        node = self.head
        if node.next is None:
            self.delete_first_node()
            return
        prev_node = None
        while node.next is not None:
            prev_node = node
            node = node.next
        prev_node.next = None
        del node
    
    def delete_a_node(self, position):
        if self.head is None:
            print('list is empty, can\'t perform delete')
            return
        i=1
        node = self.head
        while node is not None:
            if position == 1:
                del node
                return
            if i == position-1:
                to_delete_node = node.next
                node.next = to_delete_node.next
                del to_delete_node
            else:
                i+=1
    
    def get_the_middle_node(self):
        len = self.list_len()
        end = int(len/2) + 1 if len%2 == 0 else math.floor(len/2)
        prev_node = None
        current_node = self.head
        for i in range(1, end+1):
            prev_node = current_node
            current_node = current_node.next
        return prev_node
    
    def display(self):
        node = self.head
        if node is None:
            print('list is empty')
            return
        while node is not None:
            print(node.data)
            node = node.next

    def recursive_linked_list(self,head_node):
        if head_node is None or head_node.next is None:
            return head_node
        x = self.recursive_linked_list(head_node.next)
        head_node.next.next = head_node
        head_node.next = None
        return x 
    
    def list_len(self):
        if self.head is None:
            return 0
        else:
            count = 0
            current_node = self.head
            while current_node is not None:
                current_node = current_node.next
                count+=1
            return count    

    def tail_recursion(self, prev_node, head_node):
        if head_node is None or head_node.next is None:
            self.head = head_node
            head_node.next = prev_node
            return
        next_node = head_node.next 
        # head_node.next.next = head_node
        head_node.next = prev_node
        prev_node= head_node
        self.tail_recursion(head_node, next_node)

    def count_given_text(self, text):
        if self.head is None:
            return 0
        else:
            current_node = self.head
            count = 0
            while current_node is not None:
                if current_node.data == text:
                    count+=1
                current_node = current_node.next
            return count

node1 = Node('a')
node2 = Node('b')
node3 = Node('c')
node4 = Node('d')

list = LinkedList()
list.insert_at_beginning(node4)
list.insert_at_beginning(node3)
list.insert_at_beginning(node2)
list.insert_at_beginning(node1)
list.insert_at_specific_position(Node('a'),3)
list.insert_at_specific_position(Node('a'), 5)
list.insert_at_specific_position(Node('z'),1)

# list.display()
# list.delete_first_node()
# list.delete_last_node()


def reverse_list(list):
    # print('i am teher')
    prev_node = None
    next_node = None
    current_node = list.head
    while current_node is not None:
        next_node = current_node.next
        current_node.next = prev_node
        prev_node = current_node
        current_node = next_node
    list.head = prev_node

# reverse_list(list)
# list.head = list.recursive_linked_list(list.head)
# list.tail_recursion(None,list.head)

# print(list.count_given_text('z'))
print('*****************'+list.get_the_middle_node().data)
list.display()