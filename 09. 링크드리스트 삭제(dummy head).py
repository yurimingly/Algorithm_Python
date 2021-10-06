class Node:

    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = None
        self.head.next = self.tail


    def traverse(self):
        result = []
        curr = self.head
        while curr.next:
            curr = curr.next
            result.append(curr.data)
        return result


    def getAt(self, pos):
        if pos < 0 or pos > self.nodeCount:
            return None

        i = 0
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1

        return curr


    def insertAfter(self, prev, newNode):
        newNode.next = prev.next
        if prev.next is None: #prev가 맨 마지막 노드라면 tail(뒤에 노드가 없는)
            self.tail = newNode #새로운 노드를 tail로 지정하라
        prev.next = newNode
        self.nodeCount += 1
        return True


    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        if pos != 1 and pos == self.nodeCount + 1: #pos가 tail이면
            prev = self.tail
        else: #pos==0이면 head이기 때문에 위의 경우만 고려하면 됐기에 else:
            prev = self.getAt(pos - 1)
        return self.insertAfter(prev, newNode)

##############################################################
    def popAfter(self, prev):
        target = prev.next
        if target == None:
            return None
        if target.next ==None:
            if self.nodeCount==1:
                self.tail = None

            else:
                self.tail = prev

        prev.next = target.next
        self.nodeCount -= 1
        return target.data


    def popAt(self, pos):
        if pos<1 or pos>self.nodeCount:
            raise IndexError

        prev = self.getAt(pos-1)
        return self.popAfter(prev)

def solution(x):
    return 0