# https://www.acmicpc.net/problem/1697

import collections

n, k = map(int, input().split())

ans=0

q=collections.deque()

q.append(n)
graph=[0]*100001

if n == k:
    print(0)
    exit()
while q:
    cur=q.popleft()

    for x in [cur-1, cur+1, cur*2]:
        if 0<=x<100001 and graph[x]==0:
            graph[x]=graph[cur]+1
            q.append(x)
        if x==k:
            print(graph[x])
            exit()