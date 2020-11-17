class LinkedList:
    """
    Linked List implementation:
    head points to the first node
    each node will point to the next
    """

    def __init__(self, initial_list=None):
        self.head = None

        if(initial_list):
            for value in initial_list[::-1]:
                self.insert(value)

    def __str__(self):
        output = ""
        current = self.head
        while current:
            output += '{ ' + str(current) + ' } -> '
            current = current.next
        output += 'NULL'
        return output

    def includes(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def insert(self, value):
        self.head = Node(value, self.head)

    def append(self, value):
        node = Node(value)
        current = self.head
        if not current:
            self.head = node
            return

        while(current.next):
            current = current.next
        current.next = node

    def insert_before(self, new_val, reference_val):
        if not self.head:
            raise Exception('Cannot `insert_before` on empty LinkedList')

        if self.head.value == reference_val:
            self.insert(new_val)
            return

        current = self.head
        while(current.next):
            if(current.next.value == reference_val):
                current.next = Node(new_val, current.next)
                return
            current = current.next
        raise Exception(f'No node containing: {reference_val}')

    def insert_after(self, new_val, reference_val):
        if not self.head:
            raise Exception('Cannot `insert_after` on empty LinkedList')

        current = self.head
        while current:
            if current.value == reference_val:
                current.next = Node(new_val, current.next)
                return
            current = current.next
        raise Exception(f'No node containing: {reference_val}')

    def kth_from_end(self, k):
        leader = follower = self.head

        if k < 0 or not leader:
            raise Exception(f'Invalid index: {k} is out of range on linked list')

        rope = k

        while leader.next:
            leader = leader.next
            if rope:
                rope -= 1
            else:
                follower = follower.next

        if rope:
            raise Exception(f'Invalid index: {k} is out of range on linked list')
        return follower.value


class Node:
    """
    This is a Node for the LinkedList class
    value points to some value that this node is storing
    next points to the next node
    """

    def __init__(self, value=None, next_=None):
        self.value = value
        self.next = next_

    def __str__(self):
        return f'{ self.value }'


class DoubleLinkedList(LinkedList):
    """
    Double Linked List implementation
    head points to the first node
    tail points to the last node
    each node will point to the next and also the previous
    """

    def __init__(self, head=None, tail=None):
        super().__init__(head)
        self.tail = tail

    def __str__(self):
        output = "NULL"
        current = self.head
        while current:
            output += ' <-> { ' + str(current) + ' }'
            current = current.next
        output += ' <-> NULL'
        return output

    def insert(self, value):
        node = DoubleNode(value, self.head, None)
        if self.head:
            self.head.prev = node
        if not self.tail:
            self.tail = node
        self.head = node

    def append(self, value):
        node = DoubleNode(value, None, self.tail)
        if self.tail:
            self.tail.next = node
        if not self.head:
            self.head = node
        self.tail = node


class DoubleNode(Node):
    """
    This is a node for the double linked list
    value points to the value this node is responsible for holding
    next points to the next node
    prev points to the previous node
    """
    def __init__(self, value=None, next=None, prev=None):
        super().__init__(value, next)
        self.prev = prev
