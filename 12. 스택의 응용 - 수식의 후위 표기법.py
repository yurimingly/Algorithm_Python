'''
코드의 구현 - 힌트
1. 스택의 맨 위에 있는 연산자와의 우선순위 비교
 - 스택의 peek() 연산 이용
2. 스택에 남아 있는 연산자 모두 pop() 하는 순환문
 - while not opStack.isEmpty():
'''

class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}

def solution(S):
    opStack = ArrayStack()
    answer = ''
    #tmp=[]

    for var in S:
        # <prec>에 있을때
        if var in prec:
            # 비어있을때
            if opStack.isEmpty():
                opStack.push(var)
            # 스택에서 이보다 높거나 같은 우선순위는 pop
            elif var == '(':
                opStack.push(var)
            # 스택에서 이보다 작은 priority를 갖는다면 push
            elif prec[opStack.peek()] < prec[var]:
                opStack.push(var)
            # 스택에서 이보다 큰 priority를 갖는다면 pop
            else:
                while not opStack.isEmpty() and prec[opStack.peek()]>=prec[var]:
                    answer += opStack.pop()
                opStack.push(var)
        # <괄호닫기>일때
        elif var == ')':
            topToken = opStack.pop()
            while topToken != '(':
                answer += topToken
                topToken = opStack.pop()
        '''elif var == ')':
            while opStack.peek() != '(':
                answer += opStack.pop()
            opStack.pop()'''
        # <인수>일때
        else:
            answer += var
    # 남은 인자 출력
    while not opStack.isEmpty():
        answer += opStack.pop()

    return answer
