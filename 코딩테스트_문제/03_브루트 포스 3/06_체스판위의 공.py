# https://www.acmicpc.net/problem/16957
import collections
import math
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]


def bfs(x, y):
    q = collections.deque()
    q.append([x, y])
    while True:
        x, y = q.popleft()
        move = [0, 0]
        cnt = 0
        bigger = 0
        val = math.inf
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                cnt += 1
                if maps[x][y] < maps[nx][ny]:
                    bigger += 1

                if maps[nx][ny] < val:
                    val = maps[nx][ny]
                    move = [nx, ny]

        if cnt == bigger:
            return [x, y]
        if dp[move[0]][move[1]]:
            return dp[move[0]][move[1]]
        q.append(move)


dp = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        dp[i][j] = bfs(i, j)

ans = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        x, y = dp[i][j]
        ans[x][y] += 1

for i in ans:
    print(*i)
