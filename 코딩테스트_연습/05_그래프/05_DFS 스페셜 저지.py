# https://www.acmicpc.net/problem/16964
import collections

n = int(input())
graph = [[] for _ in range(n)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

arr = list(map(int, input().split()))
arr = [x - 1 for x in arr]
order = [0] * n

# 1 3 2 4
# -> 들어온 순서대로 저장
# 1 : 0
# 3 : 1
# 2 : 2
# 4 : 3
for i in range(n):
    order[arr[i]] = i

for i in range(n):
    graph[i].sort(key=lambda x: order[x])

visited = [False] * n
ans = [0]


def dfs(x):
    global ans
    visited[x] = True

    for i in graph[x]:
        if not visited[i]:
            ans.append(i)
            dfs(i)


dfs(0)
print(int(ans == arr))
