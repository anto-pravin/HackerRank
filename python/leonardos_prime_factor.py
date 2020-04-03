'''Leonardo loves primes and created  queries where each query takes the form of an integer, . For each , he wants you to count the maximum number of unique prime factors of any number in the inclusive range  and then print this value on a new line.

Note: Recall that a prime number is only divisible by  and itself, and  is not a prime number.

Input Format

The first line contains an integer, , denoting the number of queries.
Each line  of the  subsequent lines contains a single integer, .

Constraints

Output Format

For each query, print the maximum number of unique prime factors for any number in the inclusive range  on a new line.

Sample Input

6
1
2
3
500
5000
10000000000
Sample Output

0
1
1
4
5
10
'''
import os
import sys

def isprime(k):
    for i in range(2,(k//2)+1):
        if k%i == 0 and k!=2:
            return False
    return True
def primeCount(n):
    c = 0
    t = 2
    k = 1
    while n//k >= 1 and n != 1:
        if isprime(t):
            c += 1
            k *= t
            t += 1
        else:
            t += 1
        if (n//(k*t)) < 1:
            break
    return c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        result = primeCount(n)

        fptr.write(str(result) + '\n')

    fptr.close()