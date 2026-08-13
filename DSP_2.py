class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begin(self, data):
        new_node = Node(data)

        if self.head is not None:
            new_node.next = self.head
            self.head.prev = new_node

        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    def insert_at_position(self, data, position):
        new_node = Node(data)

        if position == 1:
            new_node.next = self.head

            if self.head is not None:
                self.head.prev = new_node

            self.head = new_node
            return

        temp = self.head

        for i in range(1, position - 1):
            if temp is None:
                print("Invalid position")
                return
            temp = temp.next

        if temp is None:
            print("Invalid position")
            return

        new_node.next = temp.next
        new_node.prev = temp

        if temp.next is not None:
            temp.next.prev = new_node

        temp.next = new_node

    def delete_at_begin(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head is not None:
            self.head = self.head.next

    def delete_at_end(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.prev.next = None

    def delete_at_position(self, position):
        

    def display(self):
        temp = self.head

        while temp is not None:
            print(temp.data, end=" <-> ")
            temp = temp.next

        print("None")

dll = DoublyLinkedList()

dll.insert_at_begin(20)
dll.insert_at_begin(40)
dll.insert_at_end(60)
dll.insert_at_end(80)
dll.insert_at_position(30, 3)
dll.delete_at_begin()
dll.delete_at_end()
dll.display()