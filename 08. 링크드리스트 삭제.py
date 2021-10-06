class Node:
    def __init__(self, item):
        self.data = item
        self.next = Node


class LinkedList:
    def __init__(self):
        self.nodeCount =0
        self.head=None #처음은 머리나
        self.tail=None #대가리나 아무것도 연결되어있지 않기 때문

#self는 앞선 linkedlist의 메소드이고 pos는 pos번째의 노드를 return
    def getAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            return None

        i=1
        curr = self.head
        while i <pos:
            curr = curr.next
            i+=1

    def insertAt(self,pos, newNode):
        if pos < 1 or pos > self.nodeCount +1: #pos가 올바른 위치에 안놓여져 있다면 false를 한다
            return False
        # 삽입하려는 위치가 리스트 맨 앞일때 prev는 없음. -> head의 조정이 필요하다
        if pos == 1:
            newNode.next = self.head
            self.head = newNode
        #맨 앞이 아닐때 # 전(prev)노드를 새로운 노드와 연결시킨다.
        else:
            prev = self.getAt(pos-1) # 내가 끼워 넣으려는 노드 직전에 노드를 얻어내고
            newNode.next = prev.next #
            prev.next = newNode.next
        #맨 마지막 노드일때 그 전 노드와 마지막 노드를 연결시킨다.
        if pos ==self.nodeCount + 1:
            self.tail = newNode

        self.nodeCount += 1
        return True

##############################################################
    #삭제할 그 부분의 원소 return
    def popAt(self, pos):

        if pos < 1 or pos > self.nodeCount:
            raise IndexError

        prev = self.getAt(pos - 1)
        curr = self.getAt(pos)
        if self.nodeCount == 1:
            self.head = None
            self.tail = None
        else:
            if pos == 1:
                self.head = curr.next
            elif pos == self.nodeCount:
                self.tail = prev
                prev.next = None
            else:
                prev.next = curr.next
        self.nodeCount -= 1
        return curr.data

    '''def concat(self, L):
        self.tail.next = L.head #내 원래 리스트의 맨 끝이 새로운 리스트트
       if L.tail: #만약에 새로운 연결리스트의 맨 끝이 비어있으면 안되니 if L.tail: (유효할때)
            self.tail = L.tail
        self.nodeCount += L.nodeCount'''

