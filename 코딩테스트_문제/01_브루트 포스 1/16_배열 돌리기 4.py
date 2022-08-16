# https://www.acmicpc.net/problem/17406
import copy
import itertools
import math

n, m, k = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
orders = [list(map(int, input().split())) for _ in range(k)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def solve(arr):
    temp = copy.deepcopy(maps)
    for row, col, size in arr:
        row -= 1
        col -= 1
        for s in range(1, size + 1):
            rotate = []

            # (r-s, c-s) -> (r-s, c+s)
            for c in range(col - s, col + s):
                rotate.append(temp[row - s][c])

            # (r-s, c+s) -> (r+s, c+s)
            for r in range(row - s, row + s):
                rotate.append(temp[r][col + s])

            # (r+s, c+s) -> (r+s, c-s)
            for c in range(col + s, col - s, -1):
                rotate.append(temp[row + s][c])

            # (r+s, c-s) -> (r-s, c-s)
            for r in range(row + s, row - s, -1):
                rotate.append(temp[r][col - s])

            rotate.insert(0, rotate.pop())

            idx = 0
            # (r-s, c-s) -> (r-s, c+s)
            for c in range(col - s, col + s):
                temp[row - s][c] = rotate[idx]
                idx += 1

            # (r-s, c+s) -> (r+s, c+s)
            for r in range(row - s, row + s):
                temp[r][col + s] = rotate[idx]
                idx += 1

            # (r+s, c+s) -> (r+s, c-s)
            for c in range(col + s, col - s, -1):
                temp[row + s][c] = rotate[idx]
                idx += 1

            # (r+s, c-s) -> (r-s, c-s)
            for r in range(row + s, row - s, -1):
                temp[r][col - s] = rotate[idx]
                idx += 1

    global ans
    for t in temp:
        ans = min(ans, sum(t))


ans = math.inf
for perm in itertools.permutations(orders, k):
    solve(perm)

print(ans)
