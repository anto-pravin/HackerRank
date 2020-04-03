def times(m, w, p, n):
    candy = 0
    time = 0
    while candy < n:
        temp = (p - candy) // (m * w)
        if temp <= 0:
            remaining = (candy // p) + m + w
            half = (remaining / 2)
            if m > w:
                m = max(m, half)
                w = remaining - m
            else:
                w = max(w, half)
                m = remaining - w
            candy %= p
            temp = 1
        candy += temp * m * w
        time += temp
    return int(time)

m,w,p,n = map(int,input().split())
print(times(m,w,p,n))