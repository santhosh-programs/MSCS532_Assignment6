class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        previous = None

        while current is not None and current.data != data:
            previous = current
            current = current.next

        if current is not None:
            previous.next = current.next

    def traverse(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next


if __name__ == "__main__":
    linked_list = SinglyLinkedList()
    linked_list.insert(10)
    linked_list.insert(20)
    linked_list.insert_at_beginning(5)
    linked_list.traverse()
    linked_list.delete(10)
    linked_list.traverse()
