# https://www.acmicpc.net/problem/17822
import collections

n, m, t = map(int, input().split())
maps = [collections.deque(map(int, input().split())) for _ in range(n)]
orders = [list(map(int, input().split())) for _ in range(t)]

# i, j -> (i-1, j), (i+1, j), (i, j-1), (i, j+1)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
rot = {0 : 1, 1 : -1}
# 번호가 x의 배수인 원판을 d 방향으로 k칸 회전 (d==0 시계, 1 반시계)
# 원판에 수가 남아 있으면 인접하면서 수가 같은것을 모두 지움
# 그러한 수가 있는 경우 원판에서 인접하면서 같은 수를 모두 지움
# 없는 경우에는 원판에 적힌 수의 평균을 구하고, 평균보다 큰 수에서 1 빼고, 작은수에서 1 더함

cnt = n * m
total = 0
for t in maps:
    total += sum(t)

for order in orders:
    x, d, k = order
    d = rot[d]

    for i in range(x-1, n, x):
        if maps[i]:
            maps[i].rotate(d * k)

    remove = set()
    if cnt:
        for i in range(n):
            for j in range(m):
                if maps[i][j]:
                    for k in range(4):
                        ni = i + dx[k]
                        nj = j + dy[k]

                        if 0 <= ni < n and 0 <= nj < m and maps[ni][nj]:
                            if maps[i][j] == maps[ni][nj]:
                                remove.add((i, j))
                                remove.add((ni, nj))

                    if j == 0:
                        if maps[i][0] == maps[i][m-1]:
                            remove.add((i, 0))
                            remove.add((i, m-1))

        if remove:
            for r in remove:
                total -= maps[r[0]][r[1]]
                maps[r[0]][r[1]] = None
                cnt -= 1
        else:
            avg = total / cnt

            for i in range(n):
                for j in range(m):
                    if maps[i][j]:
                        if maps[i][j] > avg:
                            maps[i][j] -= 1
                            total -= 1
                        elif maps[i][j] < avg:
                            maps[i][j] += 1
                            total += 1

print(total)