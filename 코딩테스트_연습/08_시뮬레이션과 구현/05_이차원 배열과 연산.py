# https://www.acmicpc.net/problem/17140

import collections

r, c, k = map(int, input().split())
r -= 1
c -= 1
maps = [list(map(int, input().split())) for _ in range(3)]
ans = 0


def calc_r():
    max_len = 0
    for i in range(len(maps)):
        temp = []
        cnt = collections.Counter(maps[i]).most_common()
        cnt.sort(key=lambda x: (x[1], x[0]))
        for j in cnt:
            if j[0] == 0:
                continue
            temp.append(j[0])
            temp.append(j[1])
        maps[i] = temp
        max_len = max(max_len, len(temp))

    max_len = min(100, max_len)
    for i in range(len(maps)):
        if len(maps[i]) < max_len:
            maps[i].extend([0] * (max_len - len(maps[i])))


while ans < 101:

    if len(maps) > r and len(maps[0]) > c and maps[r][c] == k:
        break

    if len(maps) >= len(maps[0]):
        calc_r()
    else:
        maps = list(zip(*maps))
        calc_r()
        maps = list(zip(*maps))
    ans += 1

if ans > 100:
    print(-1)
else:
    print(ans)
