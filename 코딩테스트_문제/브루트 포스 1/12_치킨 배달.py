# https://www.acmicpc.net/problem/15686
import itertools
import math

n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

chickens = []
homes = []
for i in range(n):
    for j in range(n):
        if maps[i][j] == 1:
            homes.append([i, j])
        if maps[i][j] == 2:
            chickens.append([i, j])

def dist(chicken):
    ret = 0

    for h in homes:
        cur = math.inf
        for c in chicken:
            temp = abs(c[0] - h[0]) + abs(c[1] - h[1])
            cur = min(cur, temp)
        ret += cur
    return ret


ans = math.inf
for chicken in itertools.combinations(chickens, m):
    ret = dist(chicken)
    ans = min(ans, ret)

print(ans)