import math
import os
import random
import re
import sys

# Complete the marsExploration function below.
def marsExploration(s):
    change = 0
    for i in range(0,len(s),3):
        if s[i]!= "S":
            change+=1
        if s[i+1]!="O":
            change+=1
        if s[i+2]!="S":
            change+=1
    return change

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
