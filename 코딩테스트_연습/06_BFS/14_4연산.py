# https://www.acmicpc.net/problem/14395

import collections

x, target = map(int, input().split())

if x == target:
    print(0)
    exit()

visited = set()
visited.add(x)

q = collections.deque()
q.append([x, ''])
limit = 10 ** 9


def bfs():
    while q:
        x, s = q.popleft()
        if x == target:
            return s
        if 0 <= x * x <= limit and x * x not in visited:
            q.append([x * x, s + '*'])
            visited.add(x * x)
        if 0 <= x + x <= limit and x + x not in visited:
            q.append([x + x, s + '+'])
            visited.add(x + x)
        if 0 <= x - x <= limit and x - x not in visited:
            q.append([x - x, s + '-'])
            visited.add(x - x)
        if x != 0 and 0 <= x // x <= limit and x // x not in visited:
            q.append([x // x, s + '/'])
            visited.add(x // x)
    return -1


print(bfs())
