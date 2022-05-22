# https://www.acmicpc.net/problem/1600
import collections
import sys
input = sys.stdin.readline

k = int(input())
m, n = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

def bfs():
    horse_x = [-1, -2, -2, -1, 1, 2, 2, 1]
    horse_y = [-2, -1, 1, 2, 2, 1, -1, -2]

    monkey_x = [-1, 1, 0, 0]
    monkey_y = [0, 0, -1, 1]

    q = collections.deque()
    visited = [[[-1] * (k+1) for _ in range(m)] for _ in range(n)]
    visited[0][0][k] = 0
    q.append([0, 0, k])
    while q:
        x, y, cnt = q.popleft()
        if x == n-1 and y == m-1:
            return visited[x][y][cnt]

        if cnt:
            for i in range(8):
                hdx = x + horse_x[i]
                hdy = y + horse_y[i]

                if 0 <= hdx < n and 0 <= hdy < m and \
                        maps[hdx][hdy] == 0 and visited[hdx][hdy][cnt-1] == -1:
                    visited[hdx][hdy][cnt-1] = visited[x][y][cnt] + 1
                    q.append([hdx, hdy, cnt - 1])

        for i in range(4):
            mdx = x + monkey_x[i]
            mdy = y + monkey_y[i]

            if 0 <= mdx < n and 0 <= mdy < m and \
                    maps[mdx][mdy] == 0 and visited[mdx][mdy][cnt] == -1:
                visited[mdx][mdy][cnt] = visited[x][y][cnt] + 1
                q.append([mdx, mdy, cnt])
    return -1

print(bfs())