# https://www.acmicpc.net/problem/2667

import collections
n=int(input())
graph=[list(map(int, input())) for _ in range(n)]

def dfs(x, y):
    global cnt
    cnt+=1
    graph[x][y]=0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n and graph[nx][ny]==1:
            dfs(nx, ny)

ans=[]
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnt=0
            dfs(i, j)
            ans.append(cnt)

print(len(ans))
for i in sorted(ans):
    print(i)