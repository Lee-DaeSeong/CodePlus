# https://www.acmicpc.net/problem/2234
import collections

m, n = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]


def bfs(x, y, group_idx):
    q = collections.deque()
    q.append([x, y])
    visited[x][y] = group_idx
    cnt = 0

    while q:
        x, y = q.popleft()
        cnt += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # maps[x][y] & (1 << i)
            # dx dy를 1, 2, 4, 8의 순서로 설정
            # 현재 위치에서 1 << i 의 bit가 없는 경우에만 지나갈 수 있음
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and not maps[x][y] & (1 << i):
                q.append([nx, ny])
                visited[nx][ny] = group_idx
    return cnt


group = [0]
group_idx = 1
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            group.append(bfs(i, j, group_idx))
            group_idx += 1

print(group_idx - 1)
print(max(group))

ans = 0
for i in range(n):
    for j in range(m):
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]

            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] != visited[i][j]:
                ans = max(ans, group[visited[nx][ny]] + group[visited[i][j]])
print(ans)
