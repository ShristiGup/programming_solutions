import math
import os
import random
import re
import sys

# Complete the cavityMap function below.
def cavityMap(grid):
    res = []
    for i in grid:
        res.append(i)
    for i in range(len(grid)):
        if i==0 or i==len(grid)-1:
            continue
        for j in range(len(grid)):
            l = []
            if j==0 or j==len(grid)-1:
                continue
            t = int(grid[i][j])
            if t>int(grid[i-1][j]) and t>int(grid[i+1][j]) and t>int(grid[i][j-1])\
            and t>int(grid[i][j+1]):
                res[i] = res[i][:j]+"X"+res[i][j+1:]
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
