
from typing import Any, Optional


class Node:
    def __init__(self, val: int):
        self.val = val
        self.next: Optional[Node] = None

class MyLinkedList:

    def __init__(self):
        self.head: Optional[Node] = None

    def get(self, index: int) -> int:
        cur = self.head
        for _ in range(index):
            if cur is None:
                return -1
            cur = cur.next
        if cur is None:
            return -1
        return cur.val

    def addAtHead(self, val: int) -> None:
        node = Node(val=val)
        node.next = self.head
        self.head = node

    def addAtTail(self, val: int) -> None:
        node_new = Node(val=val)
        if self.head is None:
            self.head = node_new
            return
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = node_new

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        node_new = Node(val=val)
        cur = self.head
        for _ in range(index - 1):
            if cur is None:
                return
            cur = cur.next
        if cur is None:
            return
        node_new.next = cur.next
        cur.next = node_new

    def deleteAtIndex(self, index: int) -> None:
        if self.head is None:
            return
        if index == 0:
            self.head = self.head.next
            return
        cur = self.head
        for _ in range(index - 1):
            if cur is None or cur.next is None:
                return
            cur = cur.next
        if cur is None or cur.next is None:
            return
        cur.next = cur.next.next            
        


if __name__ == "__main__":
    myLinkedList = MyLinkedList()
    myLinkedList.addAtHead(1)
    myLinkedList.addAtTail(3)
    myLinkedList.addAtIndex(1, 2) # linked list becomes 1->2->3
    print(myLinkedList.get(1))           # return 2
    myLinkedList.deleteAtIndex(1) # now the linked list is 1->3
    print(myLinkedList.get(1))           # return 3