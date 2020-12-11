#Using deque as Linked List

from collections import deque

LinkedList = deque()
print(LinkedList)
LinkedList.append(9)
print(LinkedList)
l = LinkedList
for i in range(11, 20):
    l.append(i)

print(LinkedList)

l.pop()
print(LinkedList)

#Creating Linked Lists manually
class Node():
    def __init__(self, data= None):
        self.data = data
        self.Next = None

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
            self.length = 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

