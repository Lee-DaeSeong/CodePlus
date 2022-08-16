# https://www.acmicpc.net/problem/16985
import collections
import copy
import itertools
import math

n = 5
maps = [[list(map(int, input().split())) for _ in range(n)] for _ in range(n)]

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]


def bfs(a):
    if not a[0][0][0] or not a[4][4][4]:
        return

    visited = [[[-1] * n for _ in range(5)] for _ in range(5)]
    q = collections.deque()
    q.append([0, 0, 0])
    visited[0][0][0] = 0
    while q:
        x, y, z = q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < n and 0 <= ny < n and 0 <= nz < n and a[nx][ny][nz] and visited[nx][ny][nz] == -1:
                visited[nx][ny][nz] = visited[x][y][z] + 1
                q.append([nx, ny, nz])

    if visited[4][4][4] == -1:
        return
    global ans
    ans = min(ans, visited[4][4][4])


def rotate(a):
    b = [[0] * 5 for _ in range(n)]
    for i in range(n):
        for j in range(n):
            b[i][j] = a[n - j - 1][i]
    return b


def dfs():
    temp = copy.deepcopy(arr)
    for _ in range(5):
        for _ in range(5):
            for _ in range(5):
                for _ in range(5):
                    for _ in range(5):
                        bfs(temp)
                        temp[0] = rotate(temp[0])
                    temp[1] = rotate(temp[1])
                temp[2] = rotate(temp[2])
            temp[3] = rotate(temp[3])
        temp[4] = rotate(temp[4])


ans = math.inf
arr = []
for orders in itertools.permutations(range(5)):
    arr = []
    for order in orders:
        arr.append(maps[order])
    dfs()

if ans == math.inf:
    ans = -1
print(ans)
