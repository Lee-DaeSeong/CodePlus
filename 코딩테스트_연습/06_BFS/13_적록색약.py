# https://www.acmicpc.net/problem/10026

import collections
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
maps=[list(input()) for _ in range(n)]

ans=[]
def dfs(x, y, c):
    dx=[-1, 1, 0, 0]
    dy=[0, 0, -1, 1]

    visited[x][y]=True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n and maps[nx][ny] == c and not visited[nx][ny]:
            dfs(nx, ny, c)

visited = [[False] * n for _ in range(n)]
r_cnt=0
for i in range(n):
    for j in range(n):
        if maps[i][j] == 'R' and not visited[i][j]:
            r_cnt+=1
            dfs(i, j, 'R')

visited = [[False] * n for _ in range(n)]
g_cnt=0
for i in range(n):
    for j in range(n):
        if maps[i][j] == 'G' and not visited[i][j]:
            g_cnt+=1
            dfs(i, j, 'G')

visited = [[False] * n for _ in range(n)]
b_cnt=0
for i in range(n):
    for j in range(n):
        if maps[i][j] == 'B' and not visited[i][j]:
            b_cnt+=1
            dfs(i, j, 'B')

print(r_cnt+g_cnt+b_cnt, end=' ')

for i in range(n):
    for j in range(n):
        if maps[i][j]=='G':
            maps[i][j]='R'
visited = [[False] * n for _ in range(n)]
rg_cnt=0
for i in range(n):
    for j in range(n):
        if maps[i][j] == 'R' and not visited[i][j]:
            rg_cnt+=1
            dfs(i, j, 'R')

print(rg_cnt + b_cnt)