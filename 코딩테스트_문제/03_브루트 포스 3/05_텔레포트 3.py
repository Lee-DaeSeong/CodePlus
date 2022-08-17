# https://www.acmicpc.net/problem/12908
import itertools
import math

sx, sy = map(int, input().split())
ex, ey = map(int, input().split())
teleport = []

for _ in range(3):
    a, b, c, d = map(int, input().split())
    teleport.append([a, b, c, d])
    teleport.append([c, d, a, b])

teleport.append([ex, ey, 0, 0])

ans = math.inf
for perm in itertools.permutations(range(7)):
    nx = sx
    ny = sy
    cur = 0
    for i in perm:
        cur += abs(nx - teleport[i][0]) + abs(ny - teleport[i][1])
        if teleport[i][0] == ex and teleport[i][1] == ey:
            break
        nx = teleport[i][2]
        ny = teleport[i][3]
        cur += 10
    ans = min(cur, ans)

print(ans)
