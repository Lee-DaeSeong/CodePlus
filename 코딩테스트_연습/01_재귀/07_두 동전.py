# https://www.acmicpc.net/problem/16197
import collections

n, m = map(int, input().split())
maps = [list(input()) for _ in range(n)]


def bfs():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while coin:
        x1, y1, x2, y2, cnt = coin.popleft()

        if cnt >= 10:
            continue

        for i in range(4):
            nx1 = x1 + dx[i]
            ny1 = y1 + dy[i]
            nx2 = x2 + dx[i]
            ny2 = y2 + dy[i]

            if 0 <= nx1 < n and 0 <= ny1 < m and 0 <= nx2 < n and 0 <= ny2 < m:
                if maps[nx1][ny1] == "#":
                    nx1, ny1 = x1, y1
                if maps[nx2][ny2] == "#":
                    nx2, ny2 = x2, y2
                coin.append((nx1, ny1, nx2, ny2, cnt + 1))
            elif (nx1 == -1 or nx1 == n or ny1 == -1 or ny1 == m) and (0 <= nx2 < n and 0 <= ny2 < m):
                return cnt + 1
            elif (nx2 == -1 or nx2 == n or ny2 == -1 or ny2 == m) and (0 <= nx1 < n and 0 <= ny1 < m):
                return cnt + 1

    return -1


temp = []
for i in range(n):
    for j in range(m):
        if maps[i][j] == 'o':
            temp.append([i, j])
            maps[i][j] = '.'

coin = collections.deque()
coin.append([temp[0][0], temp[0][1], temp[1][0], temp[1][1], 0])
print(bfs())
