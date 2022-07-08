# https://www.acmicpc.net/problem/17143

from copy import deepcopy
import sys
input = sys.stdin.readline

x, y, m = map(int, input().split())
maps = [[[] for _ in range(y)] for _ in range(x)]
# r, c, 속력, 방향, 크기
for _ in range(m):
    r, c, s, d, z = map(int, input().split())
    maps[r - 1][c - 1].append([s, d, z])

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, 1, -1]
ans = 0
ny = 0

while True:

    nx = 0
    while nx < x:
        if maps[nx][ny]:
            ans += maps[nx][ny][0][2]
            maps[nx][ny] = []
            break
        nx += 1

    if ny == y - 1:
        break

    temp = [[[] for _ in range(y)] for _ in range(x)]
    for i in range(x):
        for j in range(y):
            if maps[i][j]:
                s, d, z = maps[i][j][0]
                s_cnt = s
                r, c = i, j
                while s_cnt:
                    ni = r + dx[d]
                    nj = c + dy[d]
                    if 0 <= ni < x and 0 <= nj < y:
                        r, c = ni, nj
                        s_cnt -= 1
                    else:
                        if d in [1, 3]:
                            d += 1
                        elif d in [2, 4]:
                            d -= 1

                temp[r][c].append([s, d, z])
                if len(temp[r][c]) > 1:
                    temp[r][c] = [max(temp[r][c], key=lambda x: x[2])]

    for i in range(x):
        for j in range(y):
            maps[i][j] = temp[i][j]
    ny += 1
print(ans)