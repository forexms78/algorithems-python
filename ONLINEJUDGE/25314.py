number = int(input())
A = 'long '
B = 'int'
C = ''

time = int(number / 4)

while time > 0:
    time -= 1
    C += A

C += B

print(C)
