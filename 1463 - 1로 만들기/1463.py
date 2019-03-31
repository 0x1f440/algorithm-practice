d = 0
s = {0: {int(input())}}

while 1 not in s[d]:
    d += 1
    s[d] = set()

    for n in s[d - 1]:
        s[d].add(n - 1)
        if n % 2 == 0:
            s[d].add(n // 2)
        if n % 3 == 0:
            s[d].add(n // 3)

print(d)