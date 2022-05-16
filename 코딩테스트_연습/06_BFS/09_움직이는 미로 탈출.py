# https://www.acmicpc.net/problem/16954
import collections

maps = [list(input()) for _ in range(8)]

q = collections.deque()
q.append([7, 0])
dx = [-1, 1, 0, 0, -1, 1, -1, 1, 0]
dy = [0, 0, -1, 1, -1, 1, 1, -1, 0]


def bfs():
    while q:
        visited = [[False] * 8 for _ in range(8)]
        for _ in range(len(q)):
            x, y = q.popleft()

            if x == 0 and y == 7:
                return 1

            if maps[x][y] == '#':
                continue

            for i in range(9):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < 8 and 0 <= ny < 8 and maps[nx][ny] == '.' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append([nx, ny])

        maps.pop()
        maps.insert(0, ['.'] * 8)
    return 0


print(bfs())
