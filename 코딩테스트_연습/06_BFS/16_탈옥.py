# https://www.acmicpc.net/workbook/view/9387
import collections
import math
import sys


def bfs(x, y):
    visited = [[-1] * (m + 2) for _ in range(n + 2)]
    q = collections.deque()
    q.append([x, y])
    visited[x][y] = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n + 2 and 0 <= ny < m + 2:
                if visited[nx][ny] == -1:
                    if maps[nx][ny] == '.':
                        visited[nx][ny] = visited[x][y]
                        q.appendleft([nx, ny])
                    elif maps[nx][ny] == '#':
                        visited[nx][ny] = visited[x][y] + 1
                        q.append([nx, ny])

    return visited


t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    maps = [list(input()) for _ in range(n)]

    for i in maps:
        i.insert(0, '.')
        i.append('.')
    maps.insert(0, ['.'] * (m + 2))
    maps.append(['.'] * (m + 2))

    pos = []
    for i in range(n + 2):
        for j in range(m + 2):
            if maps[i][j] == '$':
                pos.extend([i, j])
                maps[i][j] = '.'

    x1, y1, x2, y2 = pos
    visited1 = bfs(0, 0)
    visited2 = bfs(x1, y1)
    visited3 = bfs(x2, y2)

    ans = math.inf
    for i in range(n + 2):
        for j in range(m + 2):
            if visited1[i][j] != -1 and visited2[i][j] != -1 and visited3[i][j] != -1:
                cnt = visited1[i][j] + visited2[i][j] + visited3[i][j]
                if maps[i][j] == '#':
                    cnt -= 2
                ans = min(ans, cnt)
    print(ans)
