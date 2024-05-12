# Implement a linkedlist Iteratiors
class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    def iterate_item(self):
        current_item = self.head
        while current_item:
            val = current_item.data
            current_item = current_item.next
            yield val

ll = linkedlist()
ll.insert(9)
ll.insert(98)
ll.insert("Welcome")
ll.insert(88)
ll.insert(12)

print("list")
for val in ll.iterate_item():
    print(val)
