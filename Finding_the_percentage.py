n = int(input())
d = dict()
for i in range(n):
    n = list(input().split())
    d[n[0]] = d.get(n[0],0) + ((float(n[1])+float(n[2])+float(n[3]))/3)
k = input()
print('{:.2f}'.format(d[k]))
