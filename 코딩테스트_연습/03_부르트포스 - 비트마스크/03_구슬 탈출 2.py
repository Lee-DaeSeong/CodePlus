# https://www.acmicpc.net/problem/13460
import collections

n, m = map(int, input().split())
maps = [list(input()) for _ in range(n)]
rx, ry, bx, by = 0, 0, 0, 0
for i in range(n):
    for j in range(m):
        if maps[i][j] == 'R':
            rx, ry = i, j
            maps[i][j] = '.'
        elif maps[i][j] == 'B':
            bx, by = i, j
            maps[i][j] = '.'

q = collections.deque()
q.append([rx, ry, bx, by, 0])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def move(x, y, dx, dy):
    nx, ny = x, y
    move_cnt = 0
    while True:
        if maps[nx + dx][ny + dy] != '#' and maps[nx + dx][ny + dy] != 'O':
            nx, ny = nx + dx, ny + dy
            move_cnt += 1
        else:
            break
    return nx, ny, move_cnt


def bfs():
    while q:
        rx, ry, bx, by, cnt = q.popleft()

        if cnt > 9:
            continue

        for i in range(4):
            nrx, nry, rcnt = move(rx, ry, dx[i], dy[i])
            nbx, nby, bcnt = move(bx, by, dx[i], dy[i])

            if maps[nrx + dx[i]][nry + dy[i]] == 'O' and maps[nbx + dx[i]][nby + dy[i]] != 'O':
                return cnt + 1

            if maps[nrx + dx[i]][nry + dy[i]] == 'O' and maps[nbx + dx[i]][nby + dy[i]] == 'O':
                continue

            if maps[nbx+dx[i]][nby+dy[i]] == 'O':
                continue

            if nrx == nbx and nry == nby:
                if rcnt > bcnt:
                    nrx, nry = nrx - dx[i], nry - dy[i]
                else:
                    nbx, nby = nbx - dx[i], nby - dy[i]

            if rx == nrx and ry == nry and bx == nbx and by == nby:
                continue
            q.append([nrx, nry, nbx, nby, cnt + 1])
    return -1


print(bfs())
