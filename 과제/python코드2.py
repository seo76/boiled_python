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



filename="python.txt"
rlist=[]
Plist=[]
c=0

with open(filename,"r") as file:
    for line in file:
        rlist.append(line.strip("\n"))
        c+=1
    
for i in range(c):
    rl=rlist[i]
    cont = rl
    leng = len(rl)
    capt = sum(a.isupper() for a in rl)
    lc = sum(a.islower() for a in rl)
    dc = sum(a.isdigit() for a in rl)
    schr = leng-capt-lc-dc
    node=Node(leng, capt, schr, cont)
    Plist.append(node)
    
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
            
    def insert_before(self, next_data, new_data):
        if self.head is None:
            self.head =Node(new_data)
            self.tail =self.head
            return True
        else:
            node =self.tail
            while node.data != next_data:
                node = node.prev
                if (node==Node):
                    return False

            prev_node =node.prev
            new_node =Node(new_data,prev=prev_node,next=node)
            if prev_node:
                prev_node.next =new_node
            else:
                self.head =new_node
            node.prev =new_node
            return True
        
    def insert_after(self,before_data,new_data):
        if self.head is None:
            self.head =Node(new_data)
            self.tail =self.head
            return True
        else:
            node =self.head
            while (node.data != before_data):
                node =node.next
                if node==None:
                    return False
            next_node =node.next
            new_node = Node(new_data,prev=node,next=next_node)
            if next_node:
                next_node.prev =new_node
            else:
                self.tail = new_node
            node.next =new_node

print(PPlist)
print(Node(Plist))

    




