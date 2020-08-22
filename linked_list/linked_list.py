class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def __repr__(self):
        return f"LinkedList(length={self.length}, head={self.head}"

    def __str__(self):
        output = ""
        current = self.head

        while current:
            output += f"{current.value} -> "
            current = current.next
        output += "None"

        return output

    def insert_at_head(self, data):
        """A function to insert data into the head of the LL."

        Args:
            data (Any): The data to insert.
        """
        # Creates a new node with 'next' pointing at current head of LL.
        new_node = LinkedListNode(data, self.head)

        # Reassigns the head of the LL to the new node
        self.head = new_node

        # Extends length of LL by one
        self.length += 1

    def get_by_index(self, index):
        """
        Returns the node of the LL at the specified index.

        Args:
            index (int): The index of the node to return

        Returns:
            LinkedListNode
        """
        if index < 0 or index >= self.length:
            return "accident"

        current = self.head
        for node in range(index):
            current = current.next

        return current


class LinkedListNode:
    def __init__(self, value, next):
        """A simple representation of a singular node in a linked list

        Args:
            value (Any): The value held in the node
            next (LinkedListNode): The next node in the linked list
        """
        self.value = value
        self.next = next

    def __repr__(self):
        return f"LinkedListNode(value={self.value}, next={self.next})"


# Creating a instance of the LL
linked_list = LinkedList()
linked_list.insert_at_head(10)
linked_list.insert_at_head(20)
linked_list.insert_at_head(5)

# Printing values from the LL
print(linked_list.head.value)
print(linked_list.head.next.value)
print(linked_list.get_by_index(0).value)

# Printing out representations of the LL
print(linked_list)
print(repr(linked_list))
