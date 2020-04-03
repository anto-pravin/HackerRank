n = int(input())
for _ in range(n):
    wire = 0
    a = int(input())
    distance = list(map(int,input().split()))
    cable = list(map(int,input().split()))
    for i in range(a-1):
        for j in range(i+1,a):
            k = max(cable[i],cable[j])
            wire += (k * abs(distance[i]-distance[j]))
    print(wire%1000000007)