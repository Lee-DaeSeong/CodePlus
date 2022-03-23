# https://www.acmicpc.net/problem/16931

dx = [0, 0, 0, 0, 1, -1]
dy = [0, 0, 1, -1, 0, 0]
dz = [1, -1, 0, 0, 0, 0]
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
d = [[[False] * 102 for j in range(102)] for i in range(102)]
for i in range(n):
    for j in range(m):
        for k in range(1, a[i][j] + 1):
            d[i + 1][j + 1][k] = True
ans = 0
for x in range(1, n + 1):
    for y in range(1, m + 1):
        for z in range(1, a[x - 1][y - 1] + 1):
            for k in range(6):
                nx, ny, nz = x + dx[k], y + dy[k], z + dz[k]
                if d[nx][ny][nz] == False:
                    ans += 1
print(ans)
