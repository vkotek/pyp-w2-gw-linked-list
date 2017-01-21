class Node(object):
    """
    Node class representing each of the linked nodes in the list.
    * Each node has a value and a reference to the next Node in the list.
    """

    # Initialize node, next is class
    def __init__(self, elem, next=None):
        self.elem = elem
        self.next = next
        pass

    # elem > next
    def __str__(self):
        if self.next:
            return "Node({}) > Node({})".format(self.elem, self.next.elem)
        else:
            return "Node({}) > /".format(self.elem)

    def __eq__(self, other):
        return self.elem == other.elem and self.next == other.next
    
    # When enabled things get weird and tests don't pass.
    # def __ne__(self, other):
    #     return self.elem != other.elem and self.next != other.next
        
    def __repr__(self):
        return str(self.elem)
