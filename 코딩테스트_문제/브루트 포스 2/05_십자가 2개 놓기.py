# https://www.acmicpc.net/problem/17085
import copy

n, m = map(int, input().split())
maps = [list(input()) for _ in range(n)]

ans = 0
for n1 in range(n):
    for m1 in range(m):
        if maps[n1][m1] == '#':
            temp = copy.deepcopy(maps)
            s1 = -1
            while True:
                s1 += 1
                if not (0 <= n1 - s1 and n1 + s1 < n and 0 <= m1 - s1 and m1 + s1 < m):
                    break
                if not (temp[n1 - s1][m1] == '#' and temp[n1 + s1][m1] == '#' and temp[n1][m1 - s1] == '#' and temp[n1][
                    m1 + s1] == '#'):
                    break
                temp[n1 - s1][m1] = '*'
                temp[n1 + s1][m1] = '*'
                temp[n1][m1 - s1] = '*'
                temp[n1][m1 + s1] = '*'

                for n2 in range(n):
                    for m2 in range(m):
                        s2 = -1
                        while True:
                            s2 += 1
                            if not (0 <= n2 - s2 and n2 + s2 < n and 0 <= m2 - s2 and m2 + s2 < m):
                                break
                            if not (temp[n2 - s2][m2] == '#' and temp[n2 + s2][m2] == '#' and temp[n2][
                                m2 - s2] == '#' and temp[n2][m2 + s2] == '#'):
                                break
                            ans = max(ans, ((4 * s1 + 1) * (4 * s2 + 1)))

print(ans)
