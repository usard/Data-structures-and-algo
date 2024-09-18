class Node :
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self,new_node):
        if self.head is None:
            self.head = new_node # means head points to the new node address
        else:
            prev_node = self.head # head pointed node is made as prev node
            self.head = new_node # head is pointed to new node address
            new_node.next = prev_node # new node next is pointed to prev node

    def insert_at_end(self, new_node):
        node = self.head
        while node is not None: # if node exists there will be address else it will be none
            if node.next is None:
                break
            node = node.next
        node.next = new_node    
    
    def insert_between(self, position, new_node):
        i=0
        node = self.head
        print('node at 27 :', node.data )
        if node is not None:
            while i< position-1:
                node = node.next
                print('node at 31 :', node.data)
                i+=1
            tempNode = node.next
            node.next = new_node
            new_node.next = tempNode    
     
    def delete_last_node(self):
        node  = self.head
        if node is None:
            return
        else:
            if node.next is None:
                del node
                self.head= None
            else:
                while node.next is not None:
                    print('node id :', id(node))
                    prev_node = node # both refenence same address, dont create another copy and store that copy in temp node
                    print('id of tempnode :', id(prev_node))
                    node = node.next
                prev_node.next = None
                del node
    
    def delete_node_between(self, position):
        len = self.linked_list_length()
        print('len :', len)
        if position >= int(len):
            return
        else:
            i=0
            node = self.head
            while i < position:
                prev_node = node
                print('node :', node.data)
                node = node.next
                i+=1
            prev_node.next = node.next
            del node    

    def delete_head_node(self):
        if self.head is None:
            return
        else:
            to_delete_node = self.head
            self.head = self.head.next
            del to_delete_node
    
    def search_node_data(self, element) :
        current_node = self.head
        if current_node is None:
            print('coultnot find element as the linkedlist is empty')
            return
        else:
            while current_node is not None:
                if current_node.data == element:
                    print('element found')
                    return
                else:
                    current_node = current_node.next

    # def swapPairs(head =self.head):
       
    #     if not head or not head.next:
    #         return head
    #     temp = head.next
    #     head.next = self.swapPairs(head.next.next)
    #     temp.next = head
    #     return temp     


    def linked_list_length(self):
        node =self.head
        if node is None:
           return 0
        else:
            i=0
            while node is not None:
                i+=1
                node = node.next
            return i
            
    def display(self):
        node = self.head
        while node is not None:
            print( node.data)
            node = node.next

firstNode = Node(77)
print('first node :', firstNode)
secondNode = Node(78)
thirdNode = Node(79)
lastNode = Node(80)
betweenNode = Node(81)
# print(newNode.data)
# print(newNode.next)

linkedList = LinkedList()

linkedList.insert_at_beginning(firstNode)
linkedList.insert_at_beginning(secondNode)
linkedList.insert_at_beginning(thirdNode)
linkedList.insert_at_end(lastNode)
linkedList.insert_between(2,betweenNode)
# linkedList.delete_last_node()
# linkedList.delete_node_between(4)
# linkedList.delete_head_node()
linkedList.display()
# linkedList.searh_node_data(77)

