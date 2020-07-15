"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        # create instance ListNode with value
        new_node = ListNode(value, None)
        # increment the DLL length attribute
        self.length += 1

        # if DLL is empty
            # set head and tail to the new node instance
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        # if DLL is not empty
            # set new node's next to current head
            # set head's prev to new node
            # set head to the new node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        """ First try """
        # # store the value of the head
        # value = self.head.value
        # # decrement the length of the DLL
        # self.length -= 1
        # # delete the head
        # self.delete(self.head)
        #     # if head.next is not None
        #         # set head.next.prev to None
        #         # set head to head.next
        # if self.head.next is not None:
        #     self.head.next.prev = None
        #     self.head = self.head.next
        #     # else (if head.next is None)
        #         # set head to None
        #         # set tail to None
        # else:
        #     self.head = None
        #     self.tail = None
        # # return the value
        # return value
        """ Second try """
        # if(self.head):
        #     current = self.head
        #     if self.head is self.tail:
        #         self.tail = None
        #     self.head = current.next
        #     self.length -= 1
        #     return current.value

        value = self.head.value
        self.delete(self.head)
        return value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        # create instance ListNode with value
        new_node = ListNode(value, None)
        # increment the DLL length attribute
        self.length += 1

        # if DLL is empty
            # set head and tail to the new node instance
        if not self.tail and not self.head:
            self.tail = new_node
            self.head = new_node
        # if DLL is not empty
            # set new node's prev to current tail
            # set tail's next to new node
            # set tail to the new node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        """ First try """
        # # store the value of the tail
        # value = self.tail.value
        # # decrement the length of the DLL
        # self.length -= 1
        # # delete the tail
        # self.delete(self.tail)
        #     # if tail.prev is not None
        #         # set tail.prev's prev to None
        #         # set tail to tail.prev
        # if self.tail.next is not None:
        #     self.tail.next.prev = None
        #     self.tail = self.tail.next
        #     # else (if tail.prev is None)
        #         # set head to None
        #         # set tail to None
        # else:
        #     self.head = None
        #     self.tail = None
        # # return the value
        # return value
        """ Second try """
        # curr_tail = self.tail
        # if curr_tail.prev:
        #     self.tail = curr_tail.prev
        #     new_tail = curr_tail.prev
        #     new_tail.value = None
        # else:
        #     self.tail = None
        #     self.head = None
        # self.length -= 1
        # return curr_tail.value

        value = self.tail.value
        self.delete(self.tail)
        return value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        # current = self.head
        # while current != node:
        #     current = current.next
        # if current.prev:
        #     before = current.prev
        #     before.next = current.next
        # if current.next:
        #     after = current.next
        #     after.prev = current.prev
        # prev_head = self.head
        # prev_head.prev = current
        # current.next = prev_head
        # current.prev = None
        # self.head = current

        if node is self.head:
            return
        value = node.value
        if node is self.tail:
            self.remove_from_tail()
        else:
            node.delete()
            self.length -= 1
        self.add_to_head(value)
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        current = self.head
        while current != node:
            current = current.next
        if current.prev:
            before = current.prev
            before.next = current.next
            if node == self.tail:
                self.tail = before
        if current.next:
            after = current.next
            after.prev = current.prev
            if node is self.head:
                self.head = after

        prev_tail = self.tail
        prev_tail.next = current
        current.prev = prev_tail
        current.next = None
        self.tail = current

        # if node is self.tail:
        #     return
        # value = node.value
        # if node is self.head:
        #     self.remove_from_head()
        #     self.add_to_tail

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        """ First Try """
        # current = self.head
        # while current != node:
        #     current = current.next
        # if node == self.head and node == self.tail:
        #     self.head = None
        #     self.tail = None
        # if current.prev:
        #     before = current.prev
        #     before.next = current.next
        #     if node == self.tail:
        #         self.tail = before
        # if current.next:
        #     after = current.next
        #     after.prev = current.prev
        #     if node == self.head:
        #         self.head = after
        # self.length -= 1

        if not self.head and not self.tail:
            return
        self.length -= 1 
        if self.head == self.tail:
            self.head = None
            self.tail = None
        elif self.head == node:
            self.head = node.next
            node.delete()
        elif self.tail == node:
            self.tail = node.prev
            node.delete()
        else:
            node.delete()
    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        # current = self.head
        # item = 0
        # while current:
        #     if current.value > item:
        #         item = current.value
        #     current = current.next

        # return item

        if not self.head:
            return None
        max_val = self.head.value
        current = self.head
        while current:
            if current.value > max_val:
                max_val = current.value
            current = current.next
        return max_val