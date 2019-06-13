import heapq, sys
input=sys.stdin.readline
h=[]
a=""
for _ in range(int(input())):
    n=int(input())
    if n:heapq.heappush(h, n)
    elif h:a+=str(heapq.heappop(h))+"\n"
    else:a+="0\n"
print(a)