class ArrayStack:#배열로 스택
    def __init__(self):
        self.data = []
    def size(self): #스택의 크기를 판단
        return len(self.data.)
    def isEmpty(self):#스택이 비어있는지 판단
        return self.size()==0 #불리언으로 리턴
    def push(self,item):#데이터원소를 추가
        self.data.append(item)
    def pop(self): #데이터 원소를 삭제
        return self.data.pop()
    def peek(self):#꼭대기 값을 반환
        return self.data[-1]