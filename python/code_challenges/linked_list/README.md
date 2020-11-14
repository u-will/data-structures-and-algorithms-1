# Challenge 04 - Linked List

[Pull request](https://github.com/skrambelled/data-structures-and-algorithms/pull/21)

## Problem domain:

Implement a Linked List

It should be able to insert a node at the head using O(1) time and space
It should be able to determine if a value is stored in the list
It should be able to represent all the data being stored in the node of the list

## Implementation

`LinkedList`

* `__str__` - will use a fstring to print out each ndoe
* `insert(value)` - will create a new node, insert it at the beginning of the list and set the value
* `includes(value)` - will traverse the list forwards and return a boolean `True` when the value is encountered, or `False` if never found

DoubleLinkedList

* inherits `LinkedList`
* `append(value)` - similar to `insert()`, but puts the node at the end of the list

## Future implementations:

* some method to remove a node

[<-- Python Challenges](../README.md)
