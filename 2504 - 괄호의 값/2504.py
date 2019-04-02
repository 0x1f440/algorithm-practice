# 그렇게 어렵진 않았는데 잘못된 괄호의 처리를 제대로 안 해서 틀렸었다

brackets = input()
stack = []
result = []
value = {'(': 2, '[': 3, ')': 4, ']': 6}

if len(brackets) % 2 != 0:
    print(0)
    exit(0)

for i in brackets:
    if i in ['(', '[']:
        stack.append(i)
    else:
        temp = 0
        while stack:
            x = stack.pop()
            if x in ['(', '[']:
                if value[i]/2 != value[x]:
                    print(0)
                    exit(0)
                stack.append(value[x] if temp == 0 else temp*value[x])
                break
            else:
                if not stack:
                    print(0)
                    exit(0)
                temp += x

try:
    print(sum(stack))
except TypeError:
    print(0)
