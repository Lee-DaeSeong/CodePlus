# https://www.acmicpc.net/problem/16988
import collections

n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    visited = [[False] * m for _ in range(n)]
    ret = 0

    for i in range(n):
        for j in range(m):
            if maps[i][j] == 2 and not visited[i][j]:
                q = collections.deque()
                q.append([i, j])
                visited[i][j] = True
                flag = True
                cnt = 1
                while q:
                    x, y = q.popleft()

                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]

                        if 0 <= nx < n and 0 <= ny < m:
                            if maps[nx][ny] == 0:
                                flag = False
                            if maps[nx][ny] == 2 and not visited[nx][ny]:
                                q.append([nx, ny])
                                visited[nx][ny] = True
                                cnt += 1
                if flag:
                    ret += cnt
    return ret


ans = 0
for x1 in range(n):
    for y1 in range(m):
        if maps[x1][y1] == 0:
            for x2 in range(n):
                for y2 in range(m):
                    if maps[x2][y2] == 0 and not (x1 == x2 and y1 == y2):
                        maps[x1][y1] = 1
                        maps[x2][y2] = 1
                        ans = max(ans, bfs())
                        maps[x1][y1] = 0
                        maps[x2][y2] = 0
print(ans)
