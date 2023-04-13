from Node import Node


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    # TODO: append()
    # Add to the end of the linked list
    def append(self, new_data):
        if self.head is None:  # empty linked list
            new_node = Node(new_data)
            self.head = new_node
            self.tail = new_node
        else:
            # create a new node
            new_node = Node(new_data)
            # set new node previous to tail
            new_node.previous = self.tail
            # set tail.next to new node
            self.tail.next = new_node
            # move tail to new node
            self.tail = new_node

    # TODO: insert()
    def insert(self, item, index):
        """
        insert() - insert an item at any location:
        Define function insert:
            Create a new node with whatever data needs to be stored.
            Traverse the list until the target location.
            Set the next pointer of the node left to the target to the new node's previous.
            Set the previous pointer of the node to the right of the target to the new node's next.

            And do the same with the new node's pointers.
        """
        current_node = self.head

        new_node = Node(item)
        pos = 0

        while current_node is not None:
            # Position found insert new node after it
            if pos == index:

                # Point the node at the index to the new node
                new_node.next = current_node.next
                current_node.next = new_node

                # Set the new node's "previous" pointer to the node at position index
                new_node.previous = current_node

                # Update the next node if not tail
                if new_node.next is not None:
                    new_node.next.previous = new_node

            pos += 1
            current_node = current_node.next

    # TODO: remove()
    def remove(self, value):
        """
        remove() - removes any item:
        Define function remove:
            Traverse the linked list until the target node has been found.
            For the node before the target, set the next pointer to the target's previous pointer.
            For the node after the target, set the previous pointer to the target's next pointer.
        """
        current_node = self.head

        while current_node is not None:
            if current_node.data == value:
                # Move the head pointer if needed
                if current_node == self.head:
                    self.head = current_node.next

                # Update the next pointer if not the tail
                if current_node.next is not None:
                    current_node.next.previous = current_node.previous

                # Update the previous pointer if not the old head
                if current_node.previous is not None:
                    current_node.previous.next = current_node.next
            current_node = current_node.next

    # TODO: update()
    # Find and existing node with data == item and update with new value
    # traverse to find node
    # replace the data with value
    # hint: look at find() for singly linked list
    def update(self, item, value):
        """
        update() - updates the value of an item:
        Define function update():
            Loop through the linked list until the target node's position has been found.
            If a node is found at that position, update the data.
        """
        current_node = self.head

        while current_node is not None:
            # Node found, update value and break loop
            if current_node.data == item:
                current_node.data = value
                break

            current_node = current_node.next

    # TODO: find()
    def find(self, item):
        """
        find() - finds an item:
        Define function find():
            Traverse the linked list starting from either side until the target node is found.
            If the data of one of the nodes equals the target, return that node's position.
            Otherwise, return False or null.
        """
        current_node = self.head
        pos = 0

        while current_node is not None:
            # Node found, return position
            if current_node.data == item:
                return pos

            pos += 1
            current_node = current_node.next
        # Node was not found in the list
        return -1
