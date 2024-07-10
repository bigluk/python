class CustomLinkedList:

    def __init__(self):
        self.head = None


    def add_at_beginning(self, data):
        """Add the element at the beginning of the list.

        :param data: the element to insert
        :returns: void
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node



    def add(self, data):
        """Add the element at the end of the list.

        :param data: the element to insert
        :returns: void
        """
        new_node = Node(data)
        if self.head is None:
            self.add_at_beginning(new_node)
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node



    def get(self, index):
        """Retrieve the element at the specified position in the list.

        :param index: the position of the element to retrieve
        :returns data: return the element at the specified position
        """
        if index < 0 or index is None:
            return

        current_node = self.head
        position = 0
        while (current_node is not None):
            if position == index:
                return current_node.get_data()
            position = position + 1
            current_node = current_node.next



    def remove(self, index):
        """Delete the element at the specified position in the list.

        :param index: the position of the element to delete
        :returns void
        """
        if index == 0:
            self.head = self.head.next
            return

        current_node = self.head
        position = 0
        while (current_node is not None):
            if position == index-1:
                current_node.next = current_node.next.next
                return
            position = position + 1
            current_node = current_node.next



    def length(self):
        """ Print all elements in the list """
        current_node = self.head
        length = 0
        while current_node is not None:
            length = length + 1
            current_node = current_node.next

        return length



    def print(self):
        """ Print all elements in the list """
        current_position = self.head
        while current_position is not None:
            print(current_position)
            current_position = current_position.next




class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def __str__(self):
        return str(self.data)
