from doublylinkedlist import Node
from doublylinkedlist import DoublyLinkedList

class LinkedListStack:
    def __init__(self):#비어있는 링크드리스트로 초기화
        self.data = DoublyLinkedList()
    def size(self):
        return self.data.getLength() #개수를 리턴
    def isEmpty(self):
        return self.size()==0 #isarray
    def push(self,item):
        node = Node(item)
        self.data.insertAt(self.size()+1,node) #insert 마지막에 들어가는
    def pop(self):
        return self.data.popAt(self.size()) #현재 스택에 들어있는 원소 개수를 pop
    def peek(self):
        return self.data.getAt(self.size()).data #맨 마지막에 있는 링크드리스트를 리턴