# https://www.acmicpc.net/problem/15684

m, h, n = map(int, input().split())
maps = [[0] * (m + 1) for _ in range(n + 1)]
for _ in range(h):
    a, b = map(int, input().split())
    maps[a][b] = 1
    maps[a][b + 1] = 2


def play():
    for i in range(1, m):
        r = 1
        c = i
        while r <= n:
            if maps[r][c] == 1:
                c += 1
            elif maps[r][c] == 2:
                c -= 1
            r += 1
        if i != c:
            return False
    return True


if play():
    print(0)
    exit()

ans = -1
temp = []
for i in range(1, n + 1):
    for j in range(1, m):
        if maps[i][j] == 0 and maps[i][j + 1] == 0:
            temp.append([i, j])

for i in range(len(temp)):
    x1 = temp[i][0]
    y1 = temp[i][1]
    if maps[x1][y1] != 0 or maps[x1][y1 + 1] != 0:
        continue
    maps[x1][y1] = 1
    maps[x1][y1 + 1] = 2
    if play():
        if ans == -1 or ans > 1:
            ans = 1

    for j in range(i + 1, len(temp)):
        x2 = temp[j][0]
        y2 = temp[j][1]
        if maps[x2][y2] != 0 or maps[x2][y2 + 1] != 0:
            continue
        maps[x2][y2] = 1
        maps[x2][y2 + 1] = 2
        if play():
            if ans == -1 or ans > 2:
                ans = 2

        for k in range(j + 1, len(temp)):
            x3 = temp[k][0]
            y3 = temp[k][1]
            if maps[x3][y3] != 0 or maps[x3][y3 + 1] != 0:
                continue
            maps[x3][y3] = 1
            maps[x3][y3 + 1] = 2
            if play():
                if ans == -1:
                    ans = 3

            maps[x3][y3] = 0
            maps[x3][y3 + 1] = 0

        maps[x2][y2] = 0
        maps[x2][y2 + 1] = 0

    maps[x1][y1] = 0
    maps[x1][y1 + 1] = 0

print(ans)
