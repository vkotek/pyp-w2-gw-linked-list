from .interface import *
from .node import *


class LinkedList(AbstractLinkedList):
    """
    Implementation of an AbstractLinkedList inteface.
    """

    def __init__(self, elements=None):
        
        self.start = None
        self.end = None
        
        if elements: 
            for element in elements:
               self.append(element)
        

    def __str__(self):
        return str([i for i in self])
        

    def __len__(self):
        counter = 0
        for i in self:
            counter += 1
        return counter
        

    def __iter__(self):
        
        # Start loop at first element
        current_node = self.start
        
        # For each, return element, set next to current
        while current_node:
            yield current_node.elem
            current_node = current_node.next
        
        raise StopIteration
        
        
    def __getitem__(self, index):
     
        for i, element in enumerate(iter(self)):
           if i == index:
               return element
        # Test says exception should be IndexError       
        raise IndexError
    

    def __add__(self, other):
        
        # Make sure we're adding LinkedList only
        if not isinstance(other, LinkedList):
            raise TypeError
        
        # Creates new list to append the sum of nodes to. 
        new_list = LinkedList()
        
        for i in self:
            new_list.append(i)
        
        for i in other:
            new_list.append(i)
            
        return new_list
        
        
    
    def __iadd__(self, other):
        # Addition with assignment: +=
        for i in other:
            self.append(i)
        return self
        
       

    def __eq__(self, other):
        
        # Doesn't work if length of either is 0
        if type(self) == type(other) and len(self) != len(other):
            return False
        
        for i, (a, b) in enumerate(zip(self, other)):
            if a != b:
                return False
        return True
                
                
    def __ne__(self, other):
        print(self, other)
        return not self == other

    def append(self, elem):
        
        # Elem is a single value in a list that will become a node
        # Create a node of element
        node = Node(elem)
        
        # If it has zero elements
        if self.start is None:
            self.start = node
            self.end = node
        else:
            # Node(1, None) => Node(1, Node(2, None))
            self.end.next = node
            # Node(1, None) => Node(2, None)
            self.end = node
            

    def count(self):
        return len(self)
        

    def pop(self, index=None):
        
        # Get last item if index is None
        if index == None:
            index = len(self) - 1
            
        # Make sure index is valid.
        if index not in range(len(self)):
            raise IndexError
        
        counter = 0
        current_node = self.start
        
        # Go through each node until index is hit, then perform operation
        # depending on position of index (first, last, other)
        while current_node:
            if counter == index:
                
                pop = current_node.elem
                
                # Poping first element only
                if index == 0:
                    if self.start.next is not None:
                        self.start = self.start.next
                    else: # If no next element, None.
                        self.start = None
                        
                # Poping last element
                elif index == len(self) - 1:
                    self.end = previous_node
                    self.end.next = None
                
                # Nth element
                else:
                    previous_node.next = current_node.next
                
            previous_node = current_node
            current_node = current_node.next
            counter += 1
            
        return pop
