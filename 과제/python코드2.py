"""
class Node():
    def __init__(self, data, prev=None, next=None):
        self.prev =prev #선언되면 가져오기 밑의 prev를 node-self의 prev로
        self.data =data
        self.next =next

class DLL():
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None, self.head)

    def insert(self, data):
        self.tail.next = Node(data)
        self.tail.next.prev = self.tail
        self.tail = self.tail.next

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

"""            
"""        
    def add(self, data):
        if self.head == None:
            self.head = Node(data)
            self.tail =self.head
        else:
            node = self.head
            while node.next:
                node = node.next
            new = Node(data)
            node.next = new
            new.prev = node
            self.tail = new
"""            




    




