# https://www.youtube.com/watch?v=x1KtZRuhpj8
import sys
sys.setrecursionlimit(10**9)
n = int(input())
maps = [list(input()) for _ in range(n)]

color = [[-1] * n for _ in range(n)]
dx = [-1, -1, 0, 0, 1, 1]
dy = [0, 1, -1, 1, -1, 0]
ans = 0


def dfs(x, y, c):
    global ans
    color[x][y] = c

    # X가 한개라도 존재 -> 답 1 이상
    ans = max(ans, 1)

    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if maps[nx][ny] == 'X':
                if color[nx][ny] == -1:
                    # c가 0이면 1
                    # c가 1이면 0
                    ans = max(ans, 2)
                    dfs(nx, ny, not c)

                # 현재 color랑 주변 color중 동일한 색이 있다
                # -> 0, 1 이외의 색 필요
                if color[nx][ny] == c:
                    ans = max(ans, 3)

for i in range(n):
    for j in range(n):
        if maps[i][j] == 'X' and color[i][j] == -1:
            dfs(i, j, 0)

print(ans)
