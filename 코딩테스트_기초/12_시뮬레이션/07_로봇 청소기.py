n, m = map(int, input().split())
x, y, d = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

maps[x][y] = -1
ans = 1


def turn():
    global d
    d = (d - 1) % 4


turn_cnt = 0

while True:
    for _ in range(4):
        turn()
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 0:
            maps[nx][ny] = -1
            x, y = nx, ny
            turn_cnt = 0
            ans += 1
            break
        else:
            turn_cnt += 1

    if turn_cnt == 4:
        nx = x - dx[d]
        ny = y - dy[d]

        if maps[nx][ny] != 1:
            x, y = nx, ny
            turn_cnt = 0
        else:
            break
print(ans)