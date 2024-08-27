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

    # TODO DONE
    def reverse(self):
        prev_node = None
        cur_node = self.head
        while cur_node:
            next_node = cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = next_node

        self.head = prev_node



# Voici un test de la classe LinkedList
# Tests
ll = LinkedList()
ll.append(" A ")
ll.append(" B ")
ll.append(" C ")
ll.display()  # A -> B -> C -> None
ll.reverse()
ll.display()  # C -> B -> A -> None
