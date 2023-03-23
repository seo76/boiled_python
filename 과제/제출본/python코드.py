"""class Node():
    def __init__(self, cont, leng, capt, schr, prev=None, next=None):
        self.cont = cont
        self.leng = leng
        self.capt = capt
        self.schr = schr
        self.prev = prev
        self.next = next


f=open("python.txt", 'r')
lines=f.readlines()
f.close()

Plist=[]

for line in lines:
    cont = line.strip()
    leng = len(cont)
    capt = sum(a.isupper() for a in cont)
    lc = sum(a.islower() for a in cont)
    dc = sum(a.isdigit() for a in cont)
    schr = leng-capt-lc-dc
    #print(leng, capt, schr, cont)
    node=Node(cont, leng, capt, schr)
    Plist.append(node)
    #print(node.leng)

#print(Plist)
def Lsort(node):
    return node.cont

Plist.sort(key=Lsort)
    
for node in Plist:
    print("%d,%d,%d %s"%(node.leng, node.capt, node.schr, node.cont))
"""
"""
def init(head=None, tail=None):
    self.head = Node(None,None,None,None,None,None)
    self.tail = Node(None,None,None,None,None,None)
    head.next = tail
    tail.prev = head

for node in Plist:
    node.prev = tail.prev
    node.next = tail
    tail.prev.next = node
    tail.prev = node
"""

class Node():
    def __init__(self, cont, leng, capt, schr, prev=None, next=None):
        self.cont = cont
        self.leng = leng
        self.capt = capt
        self.schr = schr
        self.prev = prev
        self.next = next


f=open("python.txt", 'r')
lines=f.readlines()
f.close()

Plist=[]

for line in lines:
    cont = line.strip()
    leng = len(cont)
    capt = sum(a.isupper() for a in cont)
    lc = sum(a.islower() for a in cont)
    dc = sum(a.isdigit() for a in cont)
    schr = leng-capt-lc-dc
    node=Node(cont, leng, capt, schr)
    Plist.append(node)

def Lsort(node):
    return node.cont

Plist.sort(key=Lsort)
    
for node in Plist:
    print("%d,%d,%d %s"%(node.leng, node.capt, node.schr, node.cont))
