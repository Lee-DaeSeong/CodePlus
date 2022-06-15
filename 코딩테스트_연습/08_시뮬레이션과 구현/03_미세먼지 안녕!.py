# https://www.acmicpc.net/problem/17144

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
n, m, t = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
temp = [[0] * m for _ in range(n)]

x = 0
y = 0
val = 0

for i in range(n):
    if maps[i][0] == -1 and maps[i + 1][0] == -1:
        x = i
        y = 0
        break


def air(start_x, start_y, z):
    prev = 0
    x = start_x
    y = start_y + 1
    k = 0
    while True:
        if x == start_x and y == start_y:
            break
        maps[x][y], prev = prev, maps[x][y]
        x += dx[k]
        y += dy[k]

        if not (0 <= x < n and 0 <= y < m):
            x -= dx[k]
            y -= dy[k]
            k += z
            k %= 4
            x += dx[k]
            y += dy[k]


while t:
    t -= 1

    for i in range(n):
        for j in range(m):
            if maps[i][j] == 0 or maps[i][j] == -1:
                continue

            cnt = 0
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]

                if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] != -1:
                    cnt += 1

            if cnt > 0:
                val = maps[i][j] // 5

                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]

                    if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] != -1:
                        temp[nx][ny] += val

            maps[i][j] -= cnt * val

    for i in range(n):
        for j in range(m):
            if maps[i][j] != -1:
                maps[i][j] += temp[i][j]
                temp[i][j] = 0

    air(x, y, 1)
    air(x + 1, y, 3)

ans = 0
for i in range(n):
    for j in range(m):
        if maps[i][j] > 0:
            ans += maps[i][j]
print(ans)
