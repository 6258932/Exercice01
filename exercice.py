class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def display(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data, end="->")
            cur_node = cur_node.next
        print(None)

    # TODO
    def reverse(self):
        node = self.head
        self.head = node.next.next
        if self.head is None:
            self.head = node
            return
        last_node = self.head
        while node.next:
            last_node = last_node.next
        last_node.next = node










# Voici un test de la classe LinkedList
# Tests
ll = LinkedList()
ll.append(" A ")
ll.append(" B ")
ll.append(" C ")
ll.display()  # A -> B -> C -> None
ll.reverse()
ll.display()  # C -> B -> A -> None
