def marcsCakewalk(calorie):
    cal = 0
    calorie.sort(reverse = True)
    for i in range(len(calorie)):
        cal+=(2**i)*calorie[i]
    return cal

n = int(input())
calorie = list(map(int,input().rstrip().split()))
result = marcsCakewalk(calorie)
print(result)
