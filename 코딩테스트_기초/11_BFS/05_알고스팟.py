import collections

m, n = map(int, input().split())
maps=[list(map(int, input())) for _ in range(n)]
q=collections.deque()
q.append([0, 0])
visited=[[False] * m for _ in range(n)]
dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]
ans=0
while q:
    x, y = q.popleft()
    if x==n-1 and y==m-1:
        print(maps[x][y])

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<n and 0<=ny<m and maps[nx][ny]==0 and not visited[nx][ny]:
            maps[nx][ny] = maps[x][y]
            q.appendleft([nx, ny])
            visited[nx][ny]=True

        elif 0<=nx<n and 0<=ny<m and maps[nx][ny]==1 and not visited[nx][ny]:
            maps[nx][ny] = maps[x][y] + 1
            q.append([nx, ny])
            visited[nx][ny]=True
