class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    
class DoublyLinkedList:
    def __init__(self):
        self.END = Node(-1)
        self.head = self.END
        self.tail = self.END
    
    def push_front(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head

        self.head.prev = new_node
        self.head = new_node
        new_node.prev = None
    
    def push_back(self, new_data):
        if self.begin() == self.end():
            self.push_front(new_data)
        
        else:
            new_node = Node(new_data)
            new_node.prev = self.tail.prev
            self.tail.prev.next = new_node
            new_node.next = self.tail
            self.tail.prev = new_node
    
    def erase(self, node):
        next_node = node.next

        if node == self.begin():
            temp = self.head
            temp.next.prev = None
            self.head = temp.next
            temp.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            node.prev = None
            node.next = None
        
        return next_node

    def insert(self, node, new_data):
        if node == self.end():
            self.push_back(new_data)
        elif node == self.begin():
            self.push_front(new_data)
        else:
            new_node = Node(new_data)
            new_node.prev = node.prev
            new_node.next = node
            node.prev.next = new_node
            node.prev = new_node
    
    def begin(self):
        return self.head
    
    def end(self):
        return self.tail

n, m = tuple(map(int, input().split()))

bread = input()

l = DoublyLinkedList()
for i in bread:
    l.push_back(i)
it = l.end()

for i in range(m):
    order = input().split()

    if order[0] == 'L':
        # 가리키는 위치 ⬆️를 바로 앞에 있는 빵을 건너뛴 위치로 변경
        if it != l.begin():
            it = it.prev
    elif order[0] == 'R':
        # 가리키는 위치 ⬆️를 바로 뒤에 있는 빵을 건너뛴 위치로 변경
        if it != l.end():
            it = it.next
    elif order[0] == 'D':
        # 가리키는 위치 ⬆️의 바로 뒤에 있는 빵을 제거
        if it.next != None:
            l.erase(it)
    elif order[0] == 'P':
        # 가리키는 위치 ⬆️에 &라는 문자가 적혀있는 식빵을 추가합니다.
        l.insert(it, order[1])
        # 이후 가리키는 위치 ⬆️는 추가된 문자 & 바로 뒤

it = l.begin()
while it != l.end():
    print(it.data, end = '')
    it = it.next