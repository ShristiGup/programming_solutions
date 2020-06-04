def gridChallenge(grid):
    for i in range(len(grid)):
        grid[i] = sorted(grid[i])
    for i in range(len(grid[0])):
        j = 0
        l = []
        while(j!=len(grid)):
            l.append(grid[j][i])
            j+=1
        if l != sorted(l):
            return "NO"
    else:
        return "YES"

t = int(input())
for _ in range(t):
    n = int(input())
    grid = []
    for i in range(n):
        item = input()
        grid.append(item)
    result = gridChallenge(grid)
    print(result)
