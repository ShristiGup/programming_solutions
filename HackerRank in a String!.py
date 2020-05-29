import math
import os
import random
import re
import sys

# Complete the hackerrankInString function below.
def hackerrankInString(s):
    w = "h"
    word = "hackerrank"
    if s.count("r")<2:
        return "NO"
    for i in word:
        if i in s:
            pass
        else:
            return "NO"
    x = s.index("h")
    m = 1
    for i in word[1:]:
        for j,v in enumerate(s):
            if i==v:
                if x<j:
                    x=j
                    w+=i
                    break
    if w==word:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
