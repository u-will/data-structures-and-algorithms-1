class LinkedList:
    """
    Linked List implementation:
    head points to the first node
    each node will point to the next
    """

    def __init__(self, head=None):
        self.head = head

    def __str__(self):
        output = ""
        current = self.head
        while current:
            output += '{ ' + str(current) + ' } -> '
            current = current.next
        output += 'NULL'
        return output

    def insert(self, value):
        node = Node(value, self.head)
        self.head = node

    def includes(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False


class Node:
    """
    This is a Node for the LinkedList class
    value points to some value that this node is storing
    next points to the next node
    """

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

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
