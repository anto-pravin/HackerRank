'''Luke is daydreaming in Math class. He has a sheet of graph paper with  rows and  columns, and he imagines that there is an army base in each cell for a total of  bases. He wants to drop supplies at strategic points on the sheet, marking each drop point with a red dot. If a base contains at least one package inside or on top of its border fence, then it's considered to be supplied. For example:


Given  and , what's the minimum number of packages that Luke must drop to supply all of his bases?

Input Format

Two space-separated integers describing the respective values of  and .

Constraints

Output Format

Print a single integer denoting the minimum number of supply packages Luke must drop.

Sample Input 0

2 2
Sample Output 0

1'''


import os
import sys

def gameWithCells(n, m):
    return(((n//2) * (m//2)) + ( ( (n%2) * m) // 2 ) + ( ((m%2) *n)//2) + ((m %2)*(n%2)))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    result = gameWithCells(n, m)

    fptr.write(str(result) + '\n')

    fptr.close()
