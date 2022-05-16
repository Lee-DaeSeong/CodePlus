# https://www.acmicpc.net/problem/16946
import collections

n, m = map(int, input().split())
maps = [list(map(int, input())) for _ in range(n)]
ans = [[0] * m for _ in range(n)]
group = [[0] * m for _ in range(n)]
group_cnt = [0]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
group_idx = 1
visited = [[False] * m for _ in range(n)]


def bfs(i, j):
    global group_idx
    q = collections.deque()
    q.append([i, j])
    cnt = 1
    visited[i][j] = True
    group[i][j] = group_idx
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] == 0:
                cnt += 1
                visited[nx][ny] = True
                group[nx][ny] = group_idx
                q.append([nx, ny])
    group_idx += 1
    group_cnt.append(cnt)


for i in range(n):
    for j in range(m):
        if maps[i][j] == 0 and not visited[i][j]:
            bfs(i, j)

for i in range(n):
    for j in range(m):
        if maps[i][j] == 1:
            near = set()
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < n and 0 <= ny < m:
                    if group[nx][ny] != 0:
                        near.add(group[nx][ny])
            temp = 1
            for t in list(near):
                temp += group_cnt[t]
            ans[i][j] = temp

for i in range(n):
    for j in range(m):
        print(ans[i][j] % 10, end='')
    print()
