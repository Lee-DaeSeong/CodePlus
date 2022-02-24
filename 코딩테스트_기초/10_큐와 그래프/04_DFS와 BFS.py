# https://www.acmicpc.net/problem/1260

import collections
import sys
sys.setrecursionlimit(10**6)
n, m, v = map(int, input().split())
graph=[[0] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b]=1
    graph[b][a]=1


def dfs(v):
    visited[v] = True
    print(v, end=' ')
    for i in range(1, n+1):
        if not visited[i] and graph[v][i] == 1:
            dfs(i)

def bfs(v):
    visited[v] = True
    q=collections.deque()
    q.append(v)
    print(v, end=' ')
    while q:
        cur = q.popleft()

        for i in range(1, n+1):
            if not visited[i] and graph[cur][i] == 1:
                print(i, end=' ')
                q.append(i)
                visited[i] = True

visited=[False] * (n+1)
dfs(v)
print()
visited=[False] * (n+1)
bfs(v)