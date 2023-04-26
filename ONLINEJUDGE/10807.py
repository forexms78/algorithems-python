total = int(input())

number = map(int,input().split())

find = int(input())

count = 0

for i in number:
    if i == find:
        count += 1

print(count)

# for i in range(type):
#     a,b = map(int,input().split())
#     total -= a*b

# if total == 0:
#     print('Yes')
# else:
#     print('No')