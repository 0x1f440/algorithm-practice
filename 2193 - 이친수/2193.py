e0, e1 = 0, 1

for i in range(int(input())-1):
	e0, e1 = e0 + e1, e0

print(e0 + e1)