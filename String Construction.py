def stringConstruction(s):
    if len(set(s)) == len(s):
        return len(s)
    cost = 0
    p = ""
    while(len(s)!=0):
        if s[0] not in p:
            p+=s[0]
            cost+=1
        s = s[1:]
    return cost


q = int(input())
for _ in range(q):
    s = input()
    result = stringConstruction(s)
    print(result)
