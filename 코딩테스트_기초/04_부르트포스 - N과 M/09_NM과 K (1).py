# https://www.acmicpc.net/problem/18290
import itertools
import math

n, m, k = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
c = [[False]*m for _ in range(n)]
ans = -math.inf
dx = [0,0,1,-1]
dy = [1,-1,0,0]

# px, py -> 이전에 선택한 칸 부터 탐색
def go(px, py, cnt, s):
    if cnt == k:
        global ans
        if ans < s:
            ans = s
        return
    for x in range(px, n):  # px 행부터 탐색
        # x == px -> 이전 행 이기 떄문에 py부터 탐색
        # x > px -> 다음 행 이기 때문에 y=0 부터 탐색
        for y in range(py if x == px else 0, m):
            if c[x][y]: #선택된 칸이면 넘어감
                continue
            flag = True
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if 0<=nx<n and 0<=ny<m:
                    if c[nx][ny]:   # nx, ny가 선택된 칸이면 선택 x (중복 불가기 때문)
                        flag = False
            if flag:
                c[x][y] = True
                go(x, y, cnt+1, s+a[x][y])
                c[x][y] = False
go(0, 0, 0, 0)
print(ans)
