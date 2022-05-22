# https://www.acmicpc.net/problem/4991
import collections
import itertools
import math

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    q = collections.deque()
    q.append([x, y])
    visited = [[-1] * m for _ in range(n)]
    visited[x][y] = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] != 'x' and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                q.append([nx, ny])
    return visited


while True:
    m, n = map(int, input().strip().split())
    if n == 0 and m == 0:
        break

    maps = [list(input().strip()) for _ in range(n)]
    dirty = []
    visited = None

    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'o':
                visited = bfs(i, j)
            if maps[i][j] == '*':
                dirty.append([i, j])

    first = [0] * len(dirty)
    check = True
    for i, xy in enumerate(dirty):
        dist = visited[xy[0]][xy[1]]
        if dist == -1:
            print(-1)
            check = False
            break
        first[i] = dist

    if check:
        dist = [[-1] * len(dirty) for _ in range(len(dirty))]
        for i in range(len(dirty)):
            visited = bfs(dirty[i][0], dirty[i][1])
            for j in range(i, len(dirty)):
                dist[i][j] = visited[dirty[j][0]][dirty[j][1]]
                dist[j][i] = dist[i][j]

        ans = math.inf
        for route in itertools.permutations(range(len(dirty))):
            temp = first[route[0]]
            start = route[0]
            for idx in range(1, len(route)):
                end = route[idx]
                temp += dist[start][end]
                start = end
            ans = min(ans, temp)

        print(ans)
