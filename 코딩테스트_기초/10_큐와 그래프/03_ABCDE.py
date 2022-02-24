# https://www.acmicpc.net/problem/13023
import collections

n, m = map(int, input().split())
maps=[[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    maps[a].append(b)
    maps[b].append(a)


def dfs(i, cnt):
    if cnt == 4:
        print(1)
        exit()

    visited[i]=True

    for j in maps[i]:
        if not visited[j]:
            dfs(j, cnt+1)
            visited[j]=False
for i in range(n):
    visited = [False] * n
    dfs(i, 0)
print(0)