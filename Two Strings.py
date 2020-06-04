def twoStrings(s1,s2):
    if set(s1) & set(s2):
        return "YES"
    else:
        return "NO"

q = int(input())
for _ in range(q):
    s1 = input()
    s2 = input()
    result = twoStrings(s1,s2)
    print(result)
