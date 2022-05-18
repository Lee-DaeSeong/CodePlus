# https://www.acmicpc.net/problem/6087
import collections

m, n = map(int, input().split())
maps = [list(input()) for _ in range(n)]

start_x, start_y, end_x, end_y = -1, -1, -1, -1

for i in range(n):
    for j in range(m):
        if maps[i][j] == 'C' and start_x == -1:
            start_x = i
            start_y = j
        elif maps[i][j] == 'C':
            end_x = i
            end_y = j

def bfs():
    visited = [[-1] * m for _ in range(n)]
    visited[start_x][start_y] = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = collections.deque()
    q.append([start_x, start_y])

    while q:
        x, y = q.popleft()

        if x == end_x and y == end_y:
            return visited[x][y] - 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            while 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] == '*':
                    break
                # 방문 x 인 경우에만 visited 갱신
                # ex)
                # -1 -1 -1 2 -1 -1
                #  1  1  1 2  1  1
                # -1 -1 -1 2 -1 -1
                if visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append([nx, ny])
                nx = nx + dx[i]
                ny = ny + dy[i]

print(bfs())
