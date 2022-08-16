# https://www.acmicpc.net/problem/17136
import math

maps = [list(map(int, input().split())) for _ in range(10)]
papers = [5] * 5


def solve(x, y, cnt):
    if x == 10:
        global ans
        ans = min(ans, cnt)
        return
    if y == 10:
        solve(x + 1, 0, cnt)
        return

    if maps[x][y] == 1:
        for size in range(5):
            flag = True
            if papers[size] > 0 and x + size < 10 and y + size < 10:
                for i in range(x, x + size + 1):
                    for j in range(y, y + size + 1):
                        if maps[i][j] == 0:
                            flag = False
            else:
                flag = False

            if not flag:
                continue

            for i in range(x, x + size + 1):
                for j in range(y, y + size + 1):
                    maps[i][j] = 0
            papers[size] -= 1
            solve(x, y + 1, cnt + 1)
            papers[size] += 1
            for i in range(x, x + size + 1):
                for j in range(y, y + size + 1):
                    maps[i][j] = 1

    else:
        solve(x, y + 1, cnt)


ans = math.inf
solve(0, 0, 0)
if ans == math.inf:
    ans = -1
print(ans)
