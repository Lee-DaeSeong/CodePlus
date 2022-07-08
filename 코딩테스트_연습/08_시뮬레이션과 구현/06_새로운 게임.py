# https://www.acmicpc.net/problem/17780

# n x n, 말 k
# 하나의 말 위에 다른 말
# 체스 판 -> 흰 빨 파
# 말 k개 놓고 시작
# 1 turn -> 1번말부터 k 번 말 까지 순서대로 이동
# 올려져 있는 말도 함께 이동, 가장 아래에 있는 말만 이동
# 말이 4개 이상 쌓이면 게임 종료

# 흰색
# 그 칸으로 이동, 이미 말이 있는 경우 가장 위에 A번 말 올려놓음
# A, B, C -> D, E -> D, E, A, B, C

# 빨간색
# 이동한 후에 A번 말과 그 위에 있는 모든 말의 쌓인 순서 변경
# A, D, F, G -> E, C, B -> E, C, B, G, F, D, A

# 이동 하려는 칸이 파란색
# A번 말의 이동 방향 반대, 한칸 이동
# 반대 이동 칸도 파란색인 경우 이동하지 않고 방향만 바꿈
# 체스판 벗어 나는 경우도 파란색과 같음

# 0 흰, 1 빨, 2 파

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
        if maps[x][y] and maps[x][y][0] != i:
            continue

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
                    maps[nx][ny] = maps[x][y]
                else:
                    maps[nx][ny].extend(maps[x][y])

            elif color[nx][ny] == 1:
                if not maps[nx][ny]:
                    maps[nx][ny] = maps[x][y][::-1]
                else:
                    maps[nx][ny].extend(maps[x][y][::-1])

        elif color[nx][ny] == 0:
            if not maps[nx][ny]:
                maps[nx][ny] = maps[x][y]
            else:
                maps[nx][ny].extend(maps[x][y])

        elif color[nx][ny] == 1:
            if not maps[nx][ny]:
                maps[nx][ny] = maps[x][y][::-1]
            else:
                maps[nx][ny].extend(maps[x][y][::-1])

        maps[x][y] = 0
        horse[i] = [nx, ny, d]
        for h in maps[nx][ny]:
            horse[h] = [nx, ny, horse[h][2]]

        if maps[nx][ny] and len(maps[nx][ny]) >= 4:
            print(ans)
            exit()

    ans += 1
print(-1)
