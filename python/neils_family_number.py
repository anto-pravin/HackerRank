import math
def neil(n):
    r = 0
    for i in n[::-1]:
        r += math.pow(int(i),len(n))
        if r > int(n):
            print('NO')
            break
    if int(r) == int(n):
        print('YES')
    print('NO')
n = input()
neil(n)