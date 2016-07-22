from .interface import AbstractLinkedList
from .node import Node


class LinkedList(AbstractLinkedList):
    """
    Implementation of an AbstractLinkedList inteface.
    """

    def __init__(self, elements=None):
        self.start = None
        self.end = None
        if elements:
            for elem in elements:
                self.append(elem)

    def __str__(self):
        return '[{}]'.format(', '.join([str(e) for e in self]))

    def __len__(self):
        return self.count()

    def __iter__(self):
        node = self.start
        while node:
            yield node.elem
            node = node.next
        raise StopIteration

    def __getitem__(self, index):
        if index >= len(self):
            raise IndexError
        for i, elem in enumerate(self):
            if i == index:
                return elem

    def __add__(self, other):
        new_list = self.__class__([elem for elem in self])
        for elem in other:
            new_list.append(elem)
        return new_list

    def __iadd__(self, other):
        for elem in other:
            self.append(elem)
        return self

    def __ne__(self, other):
        return not self.__eq__(other)

    def __eq__(self, other):
        node_a = self.start
        node_b = other.start

        while True:
            if not node_a and not node_b:
                return True

            if not bool(node_a) or not bool(node_b):
                return False

            if node_a.elem != node_b.elem:
                return False

            node_a = node_a.next
            node_b = node_b.next

    def append(self, elem):
        if self.start is None:
            self.start = Node(elem)
            self.end = self.start
            return self.start

        new_node = Node(elem)
        self.end.next = new_node
        self.end = new_node

    def count(self):
        counter = 0
        for elem in self:
            counter += 1
        return counter

    def pop(self, index=None):
        if len(self) == 0:
            # can not pop from an empty list
            raise IndexError

        if index is None:
            index = self.count() - 1

        if index >= len(self):
            raise IndexError

        if index == 0:
            elem = self.start.elem
            self.start = self.start.next
            return elem

        i = 0

        prev_node = None
        cur_node = self.start

        while True:
            if i == index:
                prev_node.next = cur_node.next
                return cur_node.elem

            prev_node = cur_node
            cur_node = cur_node.next

            i += 1
