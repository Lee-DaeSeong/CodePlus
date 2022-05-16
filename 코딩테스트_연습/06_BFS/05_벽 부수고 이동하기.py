# https://www.acmicpc.net/problem/2206
import collections
import sys

sys = sys.stdin.readline

n, m = map(int, input().split())
maps = [list(map(int, input())) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]

q = collections.deque()
q.append([0, 0, 1])

# 뚫을 수 있음
visited[0][0][1] = 1
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    while q:
        x, y, cnt = q.popleft()
        if x == n - 1 and y == m - 1:
            return visited[x][y][cnt]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                # 벽이고 뚫을 기회 있음
                if maps[nx][ny] == 1 and cnt == 1 and not visited[nx][ny][cnt]:
                    visited[nx][ny][0] = visited[x][y][1] + 1
                    q.append([nx, ny, 0])
                # 벽 아니고 방문 x
                elif maps[nx][ny] == 0 and visited[nx][ny][cnt] == 0:
                    visited[nx][ny][cnt] = visited[x][y][cnt] + 1
                    q.append([nx, ny, cnt])
    return -1

print(bfs())
