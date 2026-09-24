class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        
        new_node.next = self.head
        temp.next = new_node
        self.head = new_node

    def insert_at_end(self, data):
            new_node = Node(data)
            if not self.head:
                self.head = new_node
                new_node.next = self.head
                return
    
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
                
            temp.next = new_node
            new_node.next = self.head

    def display(self):
        if not self.head:
            print("List is empty")
            return

        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print(self.head.data)

cll = CircularLinkedList()
cll.insert_at_beginning(5)
cll.insert_at_beginning(10)
cll.insert_at_end(15)
cll.display()

