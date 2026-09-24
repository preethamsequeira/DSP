 # Creation of node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Creating LinkedList
class LinkedList:
    def __init__(self):
        self.head = None

    # insert at begin
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    # insert at the end
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # insert at given position 
    def insert_at_position(self, data, pos):
        if pos < 0:
            print("Invalid Position")
            return
        if pos == 0:
            self.insert_at_beginning(data) 
            return

        new_node = Node(data)
        current = self.head
        count = 0

        # Traverse safely up to the node right before the insertion position
        while current is not None and count < pos - 1:
            current = current.next
            count += 1
            
        if current is None:
            print("position out of range")
            return
        
        new_node.next = current.next
        current.next = new_node

    # Display the list
    def display(self):
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print("->".join(elements) if elements else "List is empty")

    
if __name__ == "__main__":
    lst = LinkedList()

    lst.insert_at_end(10)
    lst.insert_at_end(20)
    lst.insert_at_end(30)
    lst.display() 

    lst.insert_at_beginning(5)
    lst.display()  

    lst.insert_at_position(15, 2)
    lst.display() 

    lst.insert_at_position(100, 10) 
    lst.display()
