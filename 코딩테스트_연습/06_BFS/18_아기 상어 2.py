# https://www.acmicpc.net/problem/17086
import collections

n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]
visited = [[-1] * m for _ in range(n)]
q = collections.deque()

for i in range(n):
    for j in range(m):
        if maps[i][j] == 1:
            q.append([i, j])
            visited[i][j] = 0

def bfs():
    while q:
        x, y = q.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<m and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                q.append([nx, ny])

bfs()

ans = -1
for i in visited:
    ans = max(ans, max(i))

print(ans)