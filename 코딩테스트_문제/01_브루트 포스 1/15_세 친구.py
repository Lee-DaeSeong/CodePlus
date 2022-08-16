# https://www.acmicpc.net/problem/17089
import math

n, m = map(int, input().split())
graph = [[False] * (n+1) for _ in range(n+1)]
cnt = [0] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True
    cnt[a] += 1
    cnt[b] += 1

ans = math.inf
for i in range(1, n + 1):
    for j in range(i, n + 1):
        if graph[i][j]:
            for k in range(j, n + 1):
                if graph[i][k] and graph[j][k]:
                    ans = min(ans, cnt[i] + cnt[j] + cnt[k] - 6)

if ans == math.inf:
    print(-1)
else:
    print(ans)