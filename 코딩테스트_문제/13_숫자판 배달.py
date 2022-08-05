# https://www.acmicpc.net/workbook/view/9390
import collections

n = 5
maps = [list(map(int, input().split())) for _ in range(n)]

ans = collections.defaultdict(bool)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, num):
    q = collections.deque()
    q.append([x, y, str(num)])
    while q:
        x, y, num = q.popleft()

        if len(num) == 6:
            ans[num] = True
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                q.append([nx, ny, num + str(maps[nx][ny])])


for i in range(n):
    for j in range(n):
        bfs(i, j, maps[i][j])

print(len(ans))
