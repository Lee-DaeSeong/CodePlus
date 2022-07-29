# https://www.acmicpc.net/problem/19236

from copy import deepcopy

maps = [[] for _ in range(4)]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

for i in range(4):
    temp = list(map(int, input().split()))
    fish = []
    for j in range(0, len(temp), 2):
        fish.append([temp[j], temp[j + 1] - 1])
    maps[i] = fish


def dfs(sx, sy, score, maps):
    global ans
    score += maps[sx][sy][0]
    ans = max(ans, score)
    maps[sx][sy][0] = 0

    for n in range(1, 17):
        fx, fy = -1, -1
        for x in range(4):
            for y in range(4):
                if maps[x][y][0] == n:
                    fx, fy = x, y

        if fx == -1 and fy == -1:
            continue

        fd = maps[fx][fy][1]
        for i in range(8):
            nd = (fd+i) % 8
            nx = fx + dx[nd]
            ny = fy + dy[nd]

            if 0 <= nx < 4 and 0 <= ny < 4 and not (nx == sx and ny == sy):
                maps[fx][fy][1] = nd
                maps[fx][fy], maps[nx][ny] = maps[nx][ny], maps[fx][fy]
                break

    sd = maps[sx][sy][1]
    for i in range(1, 5):
        nx = sx + dx[sd] * i
        ny = sy + dy[sd] * i

        if 0 <= nx < 4 and 0 <= ny < 4 and maps[nx][ny][0] > 0:
            dfs(nx, ny, score, deepcopy(maps))

ans = 0
dfs(0, 0, 0, maps)
print(ans)
