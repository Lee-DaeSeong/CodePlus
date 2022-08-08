# https://www.acmicpc.net/problem/17069

n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]


def dfs(x, y, d):
    if x == n - 1 and y == n - 1:
        return 1

    ans = dp[x][y][d]
    if ans != -1:
        return ans
    ans = 0
    if d == 0:
        if y + 1 < n and not maps[x][y + 1]:
            ans += dfs(x, y + 1, 0)
        if x + 1 < n and y + 1 < n and not maps[x + 1][y + 1] and not maps[x + 1][y] and not maps[x][y + 1]:
            ans += dfs(x + 1, y + 1, 2)

    if d == 1:
        if x + 1 < n and not maps[x + 1][y]:
            ans += dfs(x + 1, y, 1)
        if x + 1 < n and y + 1 < n and not maps[x + 1][y + 1] and not maps[x + 1][y] and not maps[x][y + 1]:
            ans += dfs(x + 1, y + 1, 2)

    if d == 2:
        if y + 1 < n and not maps[x][y + 1]:
            ans += dfs(x, y + 1, 0)
        if x + 1 < n and not maps[x + 1][y]:
            ans += dfs(x + 1, y, 1)
        if x + 1 < n and y + 1 < n and not maps[x + 1][y + 1] and not maps[x + 1][y] and not maps[x][y + 1]:
            ans += dfs(x + 1, y + 1, 2)
    dp[x][y][d] = ans

    return ans


dp = [[[-1] * 3 for _ in range(n)] for _ in range(n)]
print(dfs(0, 1, 0))
