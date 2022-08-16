# https://www.acmicpc.net/problem/15683
import copy
import math

n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
directions = [[], [[0], [1], [2], [3]], [[0, 1], [2, 3]], [[0, 2], [2, 1], [1, 3], [3, 0]],
              [[3, 0, 2], [1, 3, 0], [2, 1, 3], [0, 2, 1]], [[0, 1, 2, 3]]]
cctv = []
for i in range(n):
    for j in range(m):
        if 1 <= maps[i][j] <= 5:
            cctv.append([i, j, maps[i][j]])


def dfs(idx, maps):
    if idx == len(cctv):
        cnt = 0
        for a in maps:
            cnt += a.count(0)
        global ans
        ans = min(ans, cnt)
        return

    temp = copy.deepcopy(maps)
    x, y, num = cctv[idx]
    for direction in directions[num]:
        for d in direction:
            nx, ny = x, y
            while True:
                nx += dx[d]
                ny += dy[d]
                if 0 <= nx < n and 0 <= ny < m:
                    if temp[nx][ny] == 6:
                        break
                    if temp[nx][ny] == 0:
                        temp[nx][ny] = -1
                else:
                    break
        dfs(idx + 1, temp)
        temp = copy.deepcopy(maps)


ans = math.inf
dfs(0, maps)
print(ans)
