'''Given integers  and , find the smallest integer , such that there exists a triangle of height , base , having an area of at least .


Input Format

In the first and only line, there are two space-separated integers  and , denoting respectively the base of a triangle and the desired minimum area.

Constraints

Output Format

In a single line, print a single integer , denoting the minimum height of a triangle with base  and area at least .

Sample Input 0

2 2
Sample Output 0

2'''

import sys
import math

def lowestTriangle(base, area):
    return math.ceil( (2 * area) / base)

base, area = input().strip().split(' ')
base, area = [int(base), int(area)]
height = lowestTriangle(base, area)
print(height)