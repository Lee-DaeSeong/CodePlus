# https://www.acmicpc.net/problem/17141

import collections
import itertools
import math
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
virus = []
maps = []
blank = 0
t = 0
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(len(temp)):
        if temp[j] == 0:
            blank += 1
        elif temp[j] == 1:
            temp[j] = -1
            t += 1
        elif temp[j] == 2:
            virus.append([i, j])
            temp[j] = 0
            blank += 1
    maps.append(temp)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    ret = 0
    cnt = 0
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1 and maps[nx][ny] == 0:
                q.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1
                ret = max(ret, visited[nx][ny])
                cnt += 1

    if blank != cnt + m:
        return -1

    return ret


ans = math.inf
for cur in itertools.combinations(virus, m):
    q = collections.deque()
    visited = [[-1] * n for _ in range(n)]
    for i in cur:
        q.append(i)
        visited[i[0]][i[1]] = 0
    ret = bfs()
    if ret == -1:
        continue
    ans = min(ans, ret)

if ans == math.inf:
    print(-1)
else:
    print(ans)
