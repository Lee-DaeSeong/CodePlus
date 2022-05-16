# https://www.acmicpc.net/problem/16928
import collections

n, m = map(int, input().split())

maps = [[] * 101 for _ in range(101)]

for _ in range(n):
    a, b = map(int, input().split())
    maps[a].append(b)

for _ in range(m):
    a, b = map(int, input().split())
    maps[a].append(b)

q = collections.deque()
q.append(1)

ans=0
visited = [0] * 101

while q:
    cur = q.popleft()
    if cur == 100:
        break
    for i in range(1, 7):
        if cur + i <= 100:
            if maps[cur + i] and not visited[maps[cur+i][0]]:
                visited[maps[cur+i][0]] = visited[cur] +1
                q.append(maps[cur+i][0])
            if not maps[cur+i] and not visited[cur+i]:
                visited[cur+i] = visited[cur] + 1
                q.append(cur+i)

print(visited[100])