#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    c=0
    k = []
    if len(s)==1:
        if m==1 and d==s[0]:
            return 1
        else:
            return 0
    else:
        for i in range(len(s)):
            if i+m > len(s):
                break
            k.append(s[i:i+m])
    for i in k:
        if sum(i) == d:
            c+=1
    return c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
