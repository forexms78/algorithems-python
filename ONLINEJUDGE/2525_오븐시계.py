def ovenTimer(a,b,c):
    b += c
    a += b // 60
    b %= 60
    if a > 23:
        k = a - 24
        a = 0
        a = a + k
    return a,b

a, b = map(int, input().split())
c = int(input())
x,y = ovenTimer(a,b,c)
print(x,y)
