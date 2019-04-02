# 쉬운데 의외로 정말 오래 걸린 문제였다.
# stack에 다른 연산자가 있는 경우, stack의 맨 위 연산자의 가중치가
# 새로 추가되는 연산자의 가중치 보다 높거나 같다면 pop해주는 부분을 제대로 못 짜서 어려웠던 듯 하다

infix = input()
postfix = ''
stack = []
operator = ['*', '/', '+', '-']
bracket = ['(', ')']


def get_priority(op) -> int:
    if op in ['*', '/']:
        return 2
    elif op in ['+', '-']:
        return 1


for i in infix:
    if i in bracket:
        if i == '(':
            stack.append(i)
        else:
            while stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()

    elif i in operator:
        if not stack:
            stack.append(i)
        else:
            while stack:
                if stack[-1] in operator and get_priority(i) <= get_priority(stack[-1]):
                    postfix += stack.pop()
                else:
                    break
            stack.append(i)
    else:
        postfix += i

while stack:
    postfix += stack.pop()

print(postfix)