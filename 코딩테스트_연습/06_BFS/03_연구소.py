# https://www.acmicpc.net/problem/14502
import collections
import copy
import itertools

n, m = map(int, input().split())

origin_maps = [list(map(int,input().split())) for _ in range(n)]

virus = collections.deque()
empty = []

for i in range(n):
    for j in range(m):
        if origin_maps[i][j] == 2:
            virus.append([i, j])
        elif origin_maps[i][j] == 0:
            empty.append([i, j])

def bfs():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q=copy.deepcopy(virus)
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<m and maps[nx][ny] == 0:
                maps[nx][ny] = 2
                q.append([nx, ny])
ans=0
for i in itertools.combinations(empty, 3):
    maps = copy.deepcopy(origin_maps)

    for a, b in i:
        maps[a][b] = 1
    bfs()
    cnt = 0
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 0:
                cnt += 1
    ans = max(ans, cnt)
print(ans)