# https://www.acmicpc.net/problem/16234
import collections

n, l, r = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    q = collections.deque()
    q.append([x, y])
    group = []
    group.append([x, y])
    people = maps[x][y]

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if l <= abs(maps[x][y] - maps[nx][ny]) <= r:
                    q.append([nx, ny])
                    group.append([nx, ny])
                    visited[nx][ny] = True
                    people += maps[nx][ny]

    if len(group) == 1:
        return False

    for x, y in group:
        maps[x][y] = people // len(group)

    return True


ans = 0
while True:
    ret = 0
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = True
                ret += bfs(i, j)
    if not ret:
        break
    ans += 1

print(ans)
