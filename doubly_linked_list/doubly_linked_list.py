"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next


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
        new_node = ListNode(value)
        # if the DLL is empty set head and tail to new node
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        # otherwise set new_node as the head and set it's prev
        # to the previous head and set that nodes next to new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            self.length += 1
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
        # check if the linked list is empty
        if self.head is None and self.tail is None:
            return None
            # check if the linked list has only one node
        if self.head == self.tail:
            # store the node we're going to remove's value
            current = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return current.value
        # otherwise set next as head, set next's prev to none, set next to none
        else:
            current = self.head
            self.head = self.head.next
            self.head.prev = None
            current.next = None
            self.length -= 1
            return current.value

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):
        new_node = ListNode(value)
        # if the DLL is empty set head and tail to new node
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        # otherwise set new_node as the head and set it's prev
        # to the previous head and set that nodes next to new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.length += 1

    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):
        # check if the linked list is empty
        if self.head is None and self.tail is None:
            return None
        # check if the linked list has only one node
        if self.head == self.tail:
            # store the node we're going to remove's value
            current = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return current.value
        else:
            current = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            current.prev = None
            self.length -= 1
            return current.value

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        pass

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        pass

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """

    def delete(self, node):
        # check if the linked list empty
        if self.head is None and self.tail is None:
            return None
        # check if there is only one linked list node
        if self.head == self.tail:
            current = self.head.value
            self.head = None
            self.tail = None
            self.length = 0
            return current
        # check if node is head
        if node.prev == None:
            self.remove_from_head()
            return self.head.value
        # check if node is tail
        if node.next == None:
            self.remove_from_tail()
            return self.tail.value
        else:
            node.next.prev = node.prev
            node.prev.next = node.next
            node.next = None
            node.prev = None
            self.length -= 1
            pass


    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """

    def get_max(self):
        if not self.head:
            return None
        # reference to the largest value we've seen so far
        max_value = self.head.value
        # reference to our current node as we traverse the list
        current = self.head.next
        # check to see if we're still at a valid list node
        while current:
            # check to see if the current value is greater than the max_value
            if current.value > max_value:
                # if so, update our max_value variable
                max_value = current.value
            # update the current node to the next node in the list
            current = current.next
        return max_value
