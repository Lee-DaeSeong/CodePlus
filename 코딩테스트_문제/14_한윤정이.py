# https://www.acmicpc.net/problem/2422
import collections
import itertools

n, m = map(int, input().split())

banned = [[False] * n for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    banned[a-1][b-1] = True
    banned[b-1][a-1] = True

ans = 0
for i in itertools.combinations(range(n), 3):
    if not banned[i[0]][i[1]] and not banned[i[0]][i[2]] and not banned[i[1]][i[2]]:
        ans += 1

print(ans)
