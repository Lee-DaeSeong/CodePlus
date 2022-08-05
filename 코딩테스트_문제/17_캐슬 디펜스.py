# https://www.acmicpc.net/problem/17406
import copy
import itertools

n, m, d = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]


def solve(archers):
    temp = copy.deepcopy(maps)

    ret = 0
    while True:
        cnt = 0
        for t in temp:
            cnt += sum(t)

        if cnt == 0:
            break

        killed = set()
        for ay in archers:
            ax = n
            cur = []
            for i in range(n):
                for j in range(m):
                    if temp[i][j]:
                        dist = abs(ax - i) + abs(ay - j)
                        if dist <= d:
                            cur.append([i, j, dist])

            if cur:
                die = tuple(min(cur, key=lambda x: (x[2], x[1]))[:2])
                killed.add(die)

        for x, y in killed:
            temp[x][y] = 0
            ret += 1
        temp.pop()
        temp.insert(0, [0] * m)

    return ret


ans = 0
for combi in itertools.combinations(range(m), 3):
    ans = max(ans, solve(combi))
print(ans)
