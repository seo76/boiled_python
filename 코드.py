
class Node:
    def __init__(self, data, prev=None, next=None):
        self.prev =prev #선언되면 가져오기 밑의 prev를 node-self의 prev로
        self.data =data
        self.next =next

class DoubleLinkedList:
    def __init__(self,data):
        self.head =Node(data)
        self.tail =self.head

    def insert(self,data):
        if (self.head==None):
            self.head =Node(data) #=앞에 뭐 없으면 초기화
            self.tail =self.head #=초기화
        else:
            node =node.head #=prev
            while (node.next):
                node =node.next #노드가 다음으로 갈 때는 다음 노드랑 연결
            new = Node(data,prev=node) #새로생성 될 때 지정
            node.next =new #그 새로 생성 되는거 뒤에 붙이기
            self.tail =new #뒤에 붙이기22

    def desc(self):
        node =self.head
        while node:
            print(node.data)
            node =node.next

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


































                    
        
