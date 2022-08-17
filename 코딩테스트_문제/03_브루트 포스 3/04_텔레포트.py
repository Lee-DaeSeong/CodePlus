# https://www.acmicpc.net/problem/16958
import collections
import math
import sys

n, t = map(int, input().split())
maps = [[] for _ in range(n)]
special = [False] * n

for i in range(n):
    s, x, y = map(int, input().split())
    special[i] = s
    maps[i] = [x - 1, y - 1]

dist = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        ix, iy = maps[i]
        jx, jy = maps[j]
        dist[i][j] = dist[j][i] = abs(ix - jx) + abs(iy - jy)


def near(x):
    d = -1
    idx = -1
    for i in range(n):
        if special[i]:
            if d == -1 or d > dist[x][i]:
                d = dist[x][i]
                idx = i
    return idx


def solve(a, b):
    d = dist[a][b]
    if special[a] and special[b]:
        d = min(d, t)

    na = near(a)  # a와 가장 가까운 특별한 도시
    nb = near(b)  # b와 가장 가까운 특별한 도시

    if na != -1 and nb != -1:
        d = min(d, dist[a][na] + t + dist[nb][b])
    return d


m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    print(solve(a - 1, b - 1))
