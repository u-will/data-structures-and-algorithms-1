from code_challenges.linked_list.linked_list import LinkedList, Node, DoubleLinkedList, DoubleNode
import pytest


def test_import():
    assert LinkedList
    assert Node
    assert DoubleLinkedList
    assert DoubleNode


def test_empty_list():
    linked_list = LinkedList()
    assert isinstance(linked_list, LinkedList)
    # test the head
    actual = linked_list.head
    expect = None
    assert actual == expect


def test_first_node():
    node = Node()
    actual = node.next
    expect = None
    assert actual == expect


def test_node(node):
    assert node.value == "some value"


def test_fixture_node_in_linked_list(one_list):
    assert isinstance(one_list.head, Node)
    assert one_list.head.value == "one"


def test_insert_node():
    linked_list = LinkedList(Node("first"))
    assert linked_list.head.value == "first"
    linked_list.insert("second")
    assert linked_list.head.value == "second"


def test_includes():
    linked_list = LinkedList(Node("first"))
    assert linked_list.includes("second") is False
    assert linked_list.includes("first") is True
    linked_list.insert("another")
    assert linked_list.includes("another") is True


def test_to_string(empty_list):
    linked_list = LinkedList()
    assert str(linked_list) == "NULL"
    linked_list.insert('3')
    linked_list.insert(2)
    linked_list.insert('1')
    assert str(linked_list) == '{ 1 } -> { 2 } -> { 3 } -> NULL'


@pytest.fixture
def empty_list():
    return LinkedList()


@pytest.fixture
def one_list():
    return LinkedList(Node("one"))


@pytest.fixture
def two_list():
    some_list = LinkedList(Node("one"))
    some_list.insert("two")
    return some_list


@pytest.fixture
def node():
    return Node("some value")


#######################
# Double linked lists #
#######################


def test_dlist():
    dlist = DoubleLinkedList()
    assert isinstance(dlist, DoubleLinkedList)


def test_insert_dlist():
    dlist = DoubleLinkedList()
    dlist.insert('1')
    assert dlist.head.value == '1'


def test_append_dlist():
    dlist = DoubleLinkedList()
    dlist.insert('1')
    dlist.append('2')
    assert dlist.tail.value == '2'


def test_str_dlist():
    dlist = DoubleLinkedList()
    dlist.insert('1')
    dlist.append('2')
    dlist.insert('3')
    dlist.append('4')
    print(str(dlist))
    assert str(dlist) == 'NULL <-> { 3 } <-> { 1 } <-> { 2 } <-> { 4 } <-> NULL'
