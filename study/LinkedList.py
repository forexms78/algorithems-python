class Node :
    def __init__(self, value = 0, next = None):
        self.value =value
        self.next = next

class LinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # 맨 뒤의 node가 new_node를 가리켜야 한다.
        else:
            self.tail.next = new_node
            self.tail = self.tail.next
            # current = self.head
            # while(current.next):
            #     current = current.next
            # current.next = new_node

    def get(self, idx):
        current = self.head
        for _ in range(idx):
            current = current.next
        return current.value

    def insert_at(self, idx, value):
        current = self.head
        # current를 넣을 인덱스 앞에 두고 인덱스에 NextAddress 값을 새로운
        # 노드의 NextAddress로 넣어준뒤 current NextAddress를 새로운
        # 노드의 value와 연결해준다.
        for _ in range(idx-1):
            current = current.next
        new_node = Node(value,current.next)
        current.next = new_node

    def remove_at(self, idx):
        current = self.head
        for _ in range(idx-1):
            current = current.next
        current.next = current.next.next
        
        
ll = LinkedList()
ll.append(9) # index 0
ll.append(8) # index 1
ll.append(7) # index 2 -> 3
ll.append(6) # index 3 -> 4
ll.insert_at(2,5) # index 2
ll.remove_at(3) # value 7 X
print(ll.get(0)) # 9
print(ll.get(1)) # 8
print(ll.get(2)) # 5
print(ll.get(3)) # 6