# https://www.acmicpc.net/problem/13913

import collections

n, k = map(int, input().split())

ans=0

q=collections.deque()

q.append(n)
graph=[0]*100001
root=[0]*100001
if n == k:
    print(0)
    print(n)
    exit()
while q:
    cur=q.popleft()

    for x in [cur-1, cur+1, cur*2]:
        if 0<=x<100001 and graph[x]==0:
            graph[x]=graph[cur]+1

            # x로 가기 위한 최소 경로는 cur을 지나야 함
            root[x]=cur
            q.append(x)
        if x==k:
            print(graph[x])

            ans=[]

            # 역추적
            while root[x] and root[x] != n:
                ans.append(root[x])
                x=root[x]
            print(*([n] + ans[::-1] + [k]))
            exit()