#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    high = scores[0]
    low = scores[0]
    b=w=0
    for i in scores[1:]:
        if i>high:
            high=i
            b+=1
        elif i<low:
            low=i
            w+=1
        else:
            pass
    l=[b,w]
    return l


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
