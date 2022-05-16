# https://www.acmicpc.net/problem/16933

import collections
import sys

input = sys.stdin.readline
n, m, k = map(int, input().split())
maps = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[[[0] * 2 for _ in range(k + 1)] for _ in range(m)] for _ in range(n)]

q = collections.deque()
q.append([0, 0, k, 0])
visited[0][0][k][0] = 1
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs():
    while q:
        x, y, cnt, time = q.popleft()
        if x == n - 1 and y == m - 1:
            return visited[x][y][cnt][time]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] == 1 and not visited[nx][ny][cnt - 1][not time] and cnt > 0 and not time:
                    visited[nx][ny][cnt - 1][not time] = visited[x][y][cnt][time] + 1
                    q.append([nx, ny, cnt - 1, not time])

                elif maps[nx][ny] == 0 and not visited[nx][ny][cnt][not time]:
                    visited[nx][ny][cnt][not time] = visited[x][y][cnt][time] + 1
                    q.append([nx, ny, cnt, not time])

        if not visited[x][y][cnt][not time]:
            visited[x][y][cnt][not time] = visited[x][y][cnt][time] + 1
            q.append([x, y, cnt, not time])
    return -1


print(bfs())
