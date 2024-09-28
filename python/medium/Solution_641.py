# 641. Design Circular Deque

class Node:
    def __init__(self, val: int, prev=None, next=None):
        self.val: int = val
        self.prev: Node = prev
        self.next: Node = prev


class MyCircularDeque:

    def __init__(self, k: int):
        self.size: int = k
        self.length: int = 0
        self.head: Node = None
        self.tail: Node = None

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.head = self.tail = Node(value)
        else:
            cur = Node(value)
            self.head.prev = cur
            cur.next = self.head
            self.head = cur
        self.length += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.head = self.tail = Node(value)
        else:
            cur = Node(value)
            self.tail.next = cur
            cur.prev = self.tail
            self.tail = cur
        self.length += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        first = self.head
        self.head = first.next
        del first
        self.length -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        last = self.tail
        self.tail = last.prev
        del last
        self.length -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.head.val

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.tail.val

    def isEmpty(self) -> bool:
        return self.length == 0

    def isFull(self) -> bool:
        return self.length == self.size


obj = MyCircularDeque(3)
print(obj.insertLast(1))
print(obj.insertLast(2))
print(obj.insertFront(3))
print(obj.insertFront(4))
print(obj.getRear())
print(obj.isEmpty())
print(obj.deleteLast())
print(obj.insertFront(4))
print(obj.getFront())
