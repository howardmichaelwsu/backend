
class SList:
    def __init__(self):
        self.head = None
    def add_to_front(self, val):
        new_node = SLNode(val)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node
        return self             
    def print_values(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next
    def add_to_back(self, val):
        if self.head == None:
            self.add_to_front(val)
            return self
        new_node = SLNode(val)
        current = self.head
        while (current.next != None):
            current = current.next
        current.next = new_node

class SLNode:
    def __init__(self, value):
        self.value = value
        self.next = None

my_list = SList()	# create a new instance of a list
my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").print_values()

