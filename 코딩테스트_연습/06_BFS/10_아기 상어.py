# https://www.acmicpc.net/problem/16236
import collections

n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]

x, y = 0, 0
for i in range(n):
    for j in range(n):
        if maps[i][j] == 9:
            x, y = i, j
            maps[i][j] = 0
            break

ans = 0
size = 2
exp = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, size):
    q = collections.deque()
    q.append([x, y])
    visited = [[-1] * n for _ in range(n)]
    visited[x][y] = 0
    ret = []
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1:
                if maps[nx][ny] == 0:
                    q.append([nx, ny])
                    visited[nx][ny] = visited[x][y] + 1
                elif maps[nx][ny] < size:
                    q.append([nx, ny])
                    visited[nx][ny] = visited[x][y] + 1
                    ret.append([visited[nx][ny], nx, ny])
                elif maps[nx][ny] == size:
                    q.append([nx, ny])
                    visited[nx][ny] = visited[x][y] + 1
    if not ret:
        return False

    ret.sort(key=lambda x: (x[0], x[1], x[2]))
    return ret[0]

while True:

    ret = bfs(x, y, size)
    if not ret:
        break
    dist, x, y = ret
    ans += dist
    maps[x][y] = 0
    exp += 1

    if exp == size:
        size += 1
        exp = 0
print(ans)
