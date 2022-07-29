# https://www.acmicpc.net/problem/19237

import sys

n, m, k = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
directions = list(map(int, input().split()))
p = [[list(map(int, input().split())) for _ in range(4)] for _ in range(m)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

smell = [[[0, 0]] * n for _ in range(n)]

def update_smell():
    for i in range(n):
        for j in range(n):
            if smell[i][j][1]:
                smell[i][j][1] -= 1
            if maps[i][j]:
                smell[i][j] = [maps[i][j], k]

def move():
    temp = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if maps[i][j] != 0:
                direction = directions[maps[i][j] - 1]
                flag = False

                for k in p[maps[i][j]-1][direction-1]:
                    nx = i + dx[k-1]
                    ny = j + dy[k-1]

                    if 0 <= nx < n and 0 <= ny < n:
                        if not smell[nx][ny][1]:
                            directions[maps[i][j] - 1] = k
                            if not temp[nx][ny]:
                                temp[nx][ny] = maps[i][j]
                            else:
                                temp[nx][ny] = min(maps[i][j], temp[nx][ny])
                            flag = True
                            break
                if flag:
                    continue

                for k in p[maps[i][j] - 1][direction - 1]:
                    nx = i + dx[k - 1]
                    ny = j + dy[k - 1]

                    if 0 <= nx < n and 0 <= ny < n and smell[nx][ny][0] == maps[i][j]:
                        directions[maps[i][j] - 1] = k
                        temp[nx][ny] = maps[i][j]
                        break
    return temp
ans = 0
while True:
    update_smell()
    ret = move()
    maps = ret
    ans += 1

    flag = True
    for i in range(n):
        for j in range(n):
            if maps[i][j] > 1:
                flag = False
    if flag:
        break

    if ans >= 1000:
        ans = -1
        break

print(ans)