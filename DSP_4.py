stack = []
def push():
    element = input("Enter an element to push onto the stack: ")
    stack.append(element)
    print(element, "pushed into stack")

def pop():
    if len(stack) == 0:
        print("Stack Underflow")
    else:
        element = stack.pop()
        print(element, "popped from stack")

def peek():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Top element:", stack[-1])

def display():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Stack elements:", stack)

while True:
    print("\n--- Stack Menu ---:")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        peek()
    elif choice == 4:
        display()
    elif choice == 5:
        break
    else:
        print("Invalid choice")