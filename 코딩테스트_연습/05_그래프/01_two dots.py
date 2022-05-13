# https://www.acmicpc.net/problem/16929
import collections

n, m = map(int, input().split())
maps = [list(input()) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(ii, jj, i, j, a, cnt):
    visited[i][j] = True

    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]

        if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == a:
            if nx == ii and ny == jj and cnt >= 3:
                print('Yes')
                exit()

            if not visited[nx][ny]:
                dfs(ii, jj, nx, ny, a, cnt + 1)

for i in range(n):
    for j in range(m):
        visited = [[False] * m for _ in range(n)]
        visited[i][j] = True
        a = maps[i][j]
        dfs(i, j, i, j, a, 0)
print('No')
