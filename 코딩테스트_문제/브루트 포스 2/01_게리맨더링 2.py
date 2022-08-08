# https://www.acmicpc.net/problem/17779
import math

n = int(input())
maps = [[0] + list(map(int, input().split())) for _ in range(n)]
maps.insert(0, [0])

total = 0
for i in maps:
    total += sum(i)


def solve(x, y, d1, d2):
    temp = [[0] * (n + 1) for _ in range(n + 1)]
    temp[x][y] = 5
    for i in range(1, d1 + 1):
        temp[x + i][y - i] = 5
    for i in range(1, d2 + 1):
        temp[x + i][y + i] = 5
    for i in range(d2 + 1):
        temp[x + d1 + i][y - d1 + i] = 5
    for i in range(d1 + 1):
        temp[x + d2 + i][y + d2 - i] = 5

    cnt = [0] * 5
    for r in range(1, x + d1):
        for c in range(1, y + 1):
            if temp[r][c] == 5:
                break
            else:
                cnt[0] += maps[r][c]

    for r in range(1, x + d2 + 1):
        for c in range(n, y, -1):
            if temp[r][c] == 5:
                break
            else:
                cnt[1] += maps[r][c]

    for r in range(x + d1, n + 1):
        for c in range(1, y - d1 + d2):
            if temp[r][c] == 5:
                break
            else:
                cnt[2] += maps[r][c]

    for r in range(x + d2 + 1, n + 1):
        for c in range(n, y - d1 + d2 - 1, -1):
            if temp[r][c] == 5:
                break
            else:
                cnt[3] += maps[r][c]

    cnt[4] = total - sum(cnt)
    return max(cnt) - min(cnt)


ans = math.inf
for x in range(1, n + 1):
    for y in range(1, n + 1):
        for d1 in range(1, n + 1):
            for d2 in range(1, n + 1):
                if 1 <= x < x + d1 + d2 <= n and 1 <= y - d1 < y < y + d2 <= n:
                    ans = min(ans, solve(x, y, d1, d2))

print(ans)
