def minion_game(s):
    v = ['a','e','i','o','u','A','E','I','O','U']
    t = list(s)
    s = 0
    k = 0
    while len(t) > 0:
        if t[0] in v:
            k += len(t)
            t.pop(0)
        else:
            s += len(t)
            t.pop(0)
    if s > k:
        print('Stuart',s)
    elif k > s:
        print('Kevin',k)
    else:
        print('Draw')
s = input()
minion_game(s)