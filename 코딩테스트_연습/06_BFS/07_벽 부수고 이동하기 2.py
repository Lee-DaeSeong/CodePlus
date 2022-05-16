# https://www.acmicpc.net/problem/14442

import collections
import sys

input = sys.stdin.readline
n, m, k = map(int, input().split())
maps = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[[0] * (k + 1) for _ in range(m)] for _ in range(n)]
q = collections.deque()
q.append([0, 0, k])
visited[0][0][k] = 1
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs():
    while q:
        x, y, cnt = q.popleft()
        if x == n - 1 and y == m - 1:
            return visited[x][y][cnt]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] == 1 and not visited[nx][ny][cnt - 1] and cnt > 0:
                    visited[nx][ny][cnt - 1] = visited[x][y][cnt] + 1
                    q.append([nx, ny, cnt - 1])
                elif maps[nx][ny] == 0 and not visited[nx][ny][cnt]:
                    visited[nx][ny][cnt] = visited[x][y][cnt] + 1
                    q.append([nx, ny, cnt])

    return -1

print(bfs())
