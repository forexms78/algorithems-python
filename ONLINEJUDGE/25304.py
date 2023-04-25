total = int(input())

type = int(input())

for i in range(type):
    a,b = map(int,input().split())
    total -= a*b

if total == 0:
    print('Yes')
else:
    print('No')