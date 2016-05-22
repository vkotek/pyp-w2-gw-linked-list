class AbstractLinkedList(object):
    """
    Abstract class representing the LinkedList inteface you must respect.
    
    You must not implement any of the method in this class, and this class
    must never be instantiated. It's just a "guide" of which methods
    the LinkedList class should respect.
    """

    def __str__(self):
        raise NotImplementedError()

    def __len__(self):
        raise NotImplementedError()

    def __iter__(self):
        raise NotImplementedError()

    def __getitem__(self, index):
        raise NotImplementedError()

    def __add__(self, other):
        raise NotImplementedError()

    def __iadd__(self, other):
        raise NotImplementedError()

    def __eq__(self, other):
        raise NotImplementedError()

    def append(self, element):
        raise NotImplementedError()

    def count(self):
        raise NotImplementedError()

    def pop(self, index=None):
        raise NotImplementedError()


class Node(object):
    """
    Node class representing each of the linked nodes in the list.
    """

    def __init__(self, elem, next=None):
        pass

    def __str__(self):
        pass

    def __eq__(self, other):
        pass

    def __repr__(self):
        pass


class LinkedList(AbstractLinkedList):
    """
    Implementation of an AbstractLinkedList inteface.
    """

    def __init__(self, elements=None):
        pass

    def __str__(self):
        pass

    def __len__(self):
        pass

    def __iter__(self):
        pass

    def __getitem__(self, index):
        pass

    def __add__(self, other):
        pass

    def __iadd__(self, other):
        pass

    def __eq__(self, other):
        pass

    def append(self, elem):
        pass

    def count(self):
        pass

    def pop(self, index=None):
        pass
