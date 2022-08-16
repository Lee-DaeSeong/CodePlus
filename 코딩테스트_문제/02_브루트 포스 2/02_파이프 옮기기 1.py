# https://www.acmicpc.net/problem/17070
import collections

n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]

q = collections.deque()
q.append([0, 1, 0])
ans = 0


def dfs(x, y, d):
    if x == n - 1 and y == n - 1:
        global ans
        ans += 1
        return
    if d == 0:
        if y + 1 < n and not maps[x][y + 1]:
            dfs(x, y + 1, 0)
        if x + 1 < n and y + 1 < n and not maps[x + 1][y + 1] and not maps[x + 1][y] and not maps[x][y + 1]:
            dfs(x + 1, y + 1, 2)

    if d == 1:
        if x + 1 < n and not maps[x + 1][y]:
            dfs(x + 1, y, 1)
        if x + 1 < n and y + 1 < n and not maps[x + 1][y + 1] and not maps[x + 1][y] and not maps[x][y + 1]:
            dfs(x + 1, y + 1, 2)

    if d == 2:
        if y + 1 < n and not maps[x][y + 1]:
            dfs(x, y + 1, 0)
        if x + 1 < n and not maps[x + 1][y]:
            dfs(x + 1, y, 1)
        if x + 1 < n and y + 1 < n and not maps[x + 1][y + 1] and not maps[x + 1][y] and not maps[x][y + 1]:
            dfs(x + 1, y + 1, 2)


dfs(0, 1, 0)
print(ans)
