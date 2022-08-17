# https://www.acmicpc.net/problem/16985

import collections
import sys
sys.setrecursionlimit(10**9)
n, m = map(int, input().split())
dic = {'U': [-1, 0], 'R': [0, 1], 'D': [1, 0], 'L': [0, -1]}

maps = [list(input()) for _ in range(n)]

def dfs(x, y):

    if not (0 <= x < n and 0 <= y < m):
        return 1

    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = 0
    move = dic[maps[x][y]]
    nx = x + move[0]
    ny = y + move[1]
    dp[x][y] = max(dp[x][y], dfs(nx, ny))
    return dp[x][y]

dp = [[-1] * m for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(m):
        if dp[i][j] == -1:
            if dfs(i, j):
                ans += 1
        elif dp[i][j] == 1:
            ans += 1

print(ans)