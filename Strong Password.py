import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    num=low=upp=sp=0
    res = 0
    for i in password:
        if i in lower_case:
            low+=1
        elif i in upper_case:
            upp+=1
        elif i in numbers:
            num+=1
        elif i in special_characters:
            sp+=1
        else:
            pass
    if low == 0:
        res=+1
    if upp == 0:
        res+=1
    if num == 0:
        res+=1
    if sp == 0:
        res+=1
    if res+len(password)<6:
        return 6-len(password)
    else:
        return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
