# https://www.acmicpc.net/problem/16948
import collections

n = int(input())

x1, y1, x2, y2 = map(int, input().split())

visited=[[0] * (n+1) for _ in range(n+1)]
q=collections.deque()
q.append([x1, y1])

dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

while q:
    x, y = q.popleft()
    if x == x2 and y == y2:
        break
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
            visited[nx][ny] = visited[x][y] + 1
            q.append([nx, ny])

if not visited[x2][y2]:
    print(-1)
else:
    print(visited[x2][y2])