# https://www.acmicpc.net/problem/16937
import itertools

h, w = map(int, input().split())
n = int(input())
stickers = [list(map(int ,input().split())) for _ in range(n)]

res = 0
for paper in itertools.combinations(stickers, 2):
    r1, c1 = paper[0]
    r2, c2 = paper[1]

    if (r1 + r2 <= h and max(c1, c2) <= w) or (max(r1, r2) <= h and c1 + c2 <= w):
        res = max(res, r1 * c1 + r2 * c2)
    if (c1 + r2 <= h and max(r1, c2) <= w) or (max(c1, r2) <= h and r1 + c2 <= w):
        res = max(res, r1 * c1 + r2 * c2)
    if (c1 + c2 <= h and max(r1, r2) <= w) or (max(c1, c2) <= h and r1 + r2 <= w):
        res = max(res, r1 * c1 + r2 * c2)
    if (r1 + c2 <= h and max(c1, r2) <= w) or (max(r1, c2) <= h and c1 + r2 <= w):
        res = max(res, r1 * c1 + r2 * c2)

print(res)