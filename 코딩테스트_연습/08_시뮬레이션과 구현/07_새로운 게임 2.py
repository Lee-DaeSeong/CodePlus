# https://www.acmicpc.net/problem/17837

n, k = map(int, input().split())
color = [list(map(int, input().split())) for _ in range(n)]
maps = [[0] * n for _ in range(n)]
horse = []

for i in range(k):
    x, y, d = map(int, input().split())
    maps[x - 1][y - 1] = [i]
    horse.append([x-1, y-1, d])

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

ans = 1
while True:

    if ans > 1000:
        ans = -1
        break

    for i in range(len(horse)):
        x, y, d = horse[i]
        cur_idx = maps[x][y].index(i)
        nx = x + dx[d]
        ny = y + dy[d]

        if not (0 <= nx < n and 0 <= ny < n) or color[nx][ny] == 2:
            if d == 1:
                d = 2
            elif d == 2:
                d = 1
            elif d == 3:
                d = 4
            elif d == 4:
                d = 3

            nx = x + dx[d]
            ny = y + dy[d]

            if not (0 <= nx < n and 0 <= ny < n) or color[nx][ny] == 2:
                horse[i] = [x, y, d]
                continue

            elif color[nx][ny] == 0:
                if not maps[nx][ny]:
                    maps[nx][ny] = maps[x][y][cur_idx:]
                else:
                    maps[nx][ny].extend(maps[x][y][cur_idx:])

            elif color[nx][ny] == 1:
                if not maps[nx][ny]:
                    maps[nx][ny] = maps[x][y][cur_idx:][::-1]
                else:
                    maps[nx][ny].extend(maps[x][y][cur_idx:][::-1])

        elif color[nx][ny] == 0:
            if not maps[nx][ny]:
                maps[nx][ny] = maps[x][y][cur_idx:]
            else:
                maps[nx][ny].extend(maps[x][y][cur_idx:])

        elif color[nx][ny] == 1:
            if not maps[nx][ny]:
                maps[nx][ny] = maps[x][y][cur_idx:][::-1]
            else:
                maps[nx][ny].extend(maps[x][y][cur_idx:][::-1])

        maps[x][y] = maps[x][y][:cur_idx]
        horse[i] = [nx, ny, d]
        for h in maps[nx][ny]:
            horse[h] = [nx, ny, horse[h][2]]

        if maps[nx][ny] and len(maps[nx][ny]) >= 4:
            print(ans)
            exit()

    ans += 1
print(-1)
