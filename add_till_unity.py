def sum_of_digit(number,s):
    if number > 0:
        rem = number %10
        s += rem
        return sum_of_digit(number //10, s)
    return s
def sum_unity(n):
    if len(str(n)) == 1:
        print(n)
        return
    else:
        t = sum_of_digit(n,0)
        return sum_unity(t)
n = int(input())
sum_unity(n)