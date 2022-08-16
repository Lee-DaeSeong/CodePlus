# https://www.acmicpc.net/problem/17471
import collections
import math

n = int(input())
peoples = [0] + list(map(int, input().split()))
maps = [[] for _ in range(n + 1)]

for i in range(1, n + 1):
    temp = list(map(int, input().split()))
    for j in range(1, len(temp)):
        maps[i].append(temp[j])

def solve(a, b):
    q = collections.deque()
    q.append(a[0])
    visited = [False] * (1 + n)
    visited[a[0]] = True
    while q:
        x = q.popleft()
        for y in maps[x]:
            if not visited[y] and y in a:
                visited[y] = True
                q.append(y)


    q = collections.deque()
    q.append(b[0])
    visited[b[0]] = True
    while q:
        x = q.popleft()
        for y in maps[x]:
            if not visited[y] and y in b:
                visited[y] = True
                q.append(y)

    for i in range(1, len(visited)):
        if not visited[i]:
            return

    global ans
    a_score = 0
    for i in a:
        a_score += peoples[i]
    b_score = 0
    for i in b:
        b_score += peoples[i]
    global ans
    ans = min(ans, abs(a_score - b_score))


def dfs(idx, a, b):
    if idx == n + 1:
        if a and b:
            solve(a, b)
        return

    dfs(idx + 1, a + [idx], b)
    dfs(idx + 1, a, b + [idx])


ans = math.inf
dfs(1, [], [])
if ans == math.inf:
    ans = -1
print(ans)
