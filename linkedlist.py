#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        self.counter = 0
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:
            self.counter += 1
            items.append(node.data)
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None # O(1) time to return a boolean variable

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(n) Beacuse we have to traverse the entire LLself.
        Condtion : If List is not empty"""
        # TODO: Loop through all nodes and count one for each
        counter = 0 # O(1) time to assign a new variable
        for item in self.items(): # O(n) for looping through entire list with no early return
            counter += 1 # O(1) for addition operation
        return counter # O(1) for returning the variable

    def length_with_counter(self):
        """Return the length of this linked list by returning the counter property.
        TODO: Running time: O(1) Because we are just returning a variable"""
        return self.counter # 0(1) for returning the counter


    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(1) Because assigning we are just assigning variables and it takes constant time
              Condition: Will be O(1) regardless of the state of the head and tail
        """
        # TODO: Create new node to hold given item
        # TODO: Append node after tail, if it exists
        new_node = Node(item) # O(1) to assign a new node
        if self.is_empty():
            self.head = new_node # O(1) to assign a new node
            self.tail = new_node # O(1) to assign a new node
            self.counter += 1 # O(1) for the addition operation
        else:
            self.tail.next = new_node # O(1) to assign a new node
            self.tail = new_node # O(1) to assign a new node
            self.counter += 1 # O(1) for the addition operation

    def prepend(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(1) Because assigning we are just assigning variables and it takes constant time
              Condition: Will be O(1) regardless of the state of the head and tail
        """
        # TODO: Create new node to hold given item
        # TODO: Prepend node before head, if it exists

        new_node = Node(item) # O(1) to assign a new node
        if self.is_empty():
            self.head = new_node # O(1) to assign a new node
            self.tail = new_node # O(1) to assign a new node
            self.counter += 1 # O(1) for the addition operation
        else:
            new_node.next = self.head # O(1) to assign a new node
            self.head = new_node # O(1) to assign a new node
            self.counter += 1 # O(1) for the addition operation


    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        TODO: Best case running time: O(1) Because it is constant time if the current_node head or near hed
        TODO: Worst case running time: O(n) Because it will take linear time if the current_node is in the tail
                                        Or not in the linkedlist
        """
        # TODO: Loop through all nodes to find item where quality(item) is True
        # TODO: Check if node's data satisfies given quality function

        current_node = self.head # O(1) to assign a new node
        while current_node is not None: # O(n) to trasverse the entire linked list
            if quality(current_node.data) == True:
                return current_node.data # O(1)  to return a node variable
            current_node = current_node.next # O(1) to assign a new node

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(1) Beacuse if item is in head or list is empty
        TODO: Worst case running time: O(n) Beacuse if item is in tail then will traverse entire list
                                        Or if item is not in list
        """

        # checks if the list is empty
        if self.is_empty():
            raise ValueError("Empty List")

        # check if item is in head
        if self.head.data == item:
            self.head = self.head.next

            #checks if the head and tail point to same object(ll with one item)
            if self.tail.data == item:
                self.tail = None
            self.counter -= 1
            return

        current_node = self.head
        # checks one node ahead
        while current_node.next is not None:# O(n) to trasverse the entire linkedlist
            if current_node.next.data == item:
                target_node = current_node.next # stores the node that contains the item
                connecting_node = target_node.next # stores the node that comes after the target node
                current_node.next = connecting_node # connects the current node and the node after target
                self.counter -= 1
                #checks if deleted node was the tail
                if self.tail.data == item:
                    #updates the tail
                    self.tail = current_node
                return
            current_node = current_node.next

        raise ValueError('Item not found: {}'.format(item))


    def replace(self, old_item, new_item):
        """Replace the given old item from this doubly linked list with the new item.
        TODO: Best case running time: O(1) If new_item is in head or tail with  early return"""

        # Checks if the old_item is the first or last node in the linkedlist
        if self.head.data == old_item:
            self.head.data = new_item
            return
        elif self.tail.data == old_item:
            self.tail.data == new_item
            return

        current_node = self.head
        while current_node is not None: # O(n) traversing the entire list
            if current_node.data == old_item:
                current_node.data = new_item
                return
            current_node = current_node.next

        raise ValueError("Old item was not found")


def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
