# https://www.acmicpc.net/problem/16947
import sys
import collections
sys.setrecursionlimit(10**9)

n = int(input())
maps = [[] for _ in range(n)]

for _ in range(n):
    a, b = map(int, input().split())
    maps[a-1].append(b-1)
    maps[b-1].append(a-1)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(start, cur, cnt):
    global ret
    visited[cur] = True

    for i in maps[cur]:
        if not visited[i]:
            dfs(start, i, cnt + 1)

        if i == start and cnt >= 2:
            ret = True

ans = [-1] * n
q=collections.deque()
for i in range(n):
    visited = [False] * n
    ret = False
    dfs(i, i, 0)
    if ret:
        ans[i] = 0
        q.append(i)

while q:
    cur = q.popleft()
    for i in maps[cur]:
        if ans[i] == -1:
            ans[i] = ans[cur] + 1
            q.append(i)

print(*ans)