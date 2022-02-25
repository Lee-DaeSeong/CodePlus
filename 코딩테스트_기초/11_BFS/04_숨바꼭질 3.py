# https://www.acmicpc.net/problem/13549

import collections

n, k = map(int, input().split())

ans=0

q=collections.deque()

q.append(n)
max_num=100001
graph=[0]*max_num
visited = [False] * max_num
visited[n] = True
if n == k:
    print(0)
    exit()
while q:
    cur=q.popleft()

    if cur * 2 < max_num and not visited[cur*2]:
        graph[cur*2]=graph[cur]
        visited[cur*2]=True
        q.appendleft(cur*2)
        if cur*2==k:
            print(graph[cur*2])
            exit()
    for x in [cur-1, cur+1]:
        if 0<=x<max_num and not visited[x]:
            graph[x]=graph[cur]+1
            visited[x] = True
            q.append(x)
        if x==k:
            print(graph[x])
            exit()