# https://www.acmicpc.net/problem/16940
import collections

n = int(input())
graph = [[] for _ in range(n)]

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

arr = list(map(int, input().split()))
arr = [x-1 for x in arr]
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
    graph[i].sort(key=lambda x:order[x])

q = collections.deque()
q.append(0)
visited=[False] * n
visited[0]=True
ans=[0]

while q:
    cur = q.popleft()
    for i in graph[cur]:
        if not visited[i]:
            visited[i] = True
            ans.append(i)
            q.append(i)

print(int(ans == arr))