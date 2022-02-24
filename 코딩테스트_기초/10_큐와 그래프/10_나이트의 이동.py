# https://www.acmicpc.net/problem/7562

import collections

t=int(input())

for _ in range(t):
    l=int(input())
    graph=[[0]*l for _ in range(l)]
    x, y = map(int, input().split())
    target_x, target_y = map(int, input().split())

    dx=[2, 1, -1, -2, -2, -1, 1, 2]
    dy=[1, 2, 2, 1, -1, -2, -2, -1]

    q=collections.deque()
    q.append([x, y])
    graph[x][y]=0
    while q:
        x, y = q.popleft()
        if x == target_x and y == target_y:
            print(graph[x][y])
            break

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<l and 0<=ny<l and graph[nx][ny] == 0:
                q.append([nx, ny])
                graph[nx][ny] = graph[x][y]+1