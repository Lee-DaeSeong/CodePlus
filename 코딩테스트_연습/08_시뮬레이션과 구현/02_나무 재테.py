# https://www.acmicpc.net/problem/16235
import collections

n, m, k = map(int, input().split())

energy = [[5] * n for _ in range(n)]
plus = [list(map(int, input().split())) for _ in range(n)]
tree = [[[] for _ in range(n)] for _ in range(n)]

for _ in range(m):
    x, y, z = map(int, input().split())
    tree[x - 1][y - 1].append(z)

dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, 1, -1, 1, 1, -1, -1]


def ss():
    for i in range(n):
        for j in range(n):
            if tree[i][j]:
                tree[i][j].sort()
                live = []
                dead_energy = 0
                for age in tree[i][j]:
                    if age <= energy[i][j]:
                        energy[i][j] -= age
                        age += 1
                        live.append(age)
                    else:
                        dead_energy += age // 2

                energy[i][j] += dead_energy
                tree[i][j] = live


def fw():
    for i in range(n):
        for j in range(n):
            if tree[i][j]:
                for age in tree[i][j]:
                    if age % 5 == 0:
                        for d in range(8):
                            nx = i + dx[d]
                            ny = j + dy[d]
                            if 0 <= nx < n and 0 <= ny < n:
                                tree[nx][ny].append(1)

    for i in range(n):
        for j in range(n):
            energy[i][j] += plus[i][j]


for _ in range(k):
    ss()
    fw()

ans = 0
for i in range(n):
    for j in range(n):
        ans += len(tree[i][j])
print(ans)
