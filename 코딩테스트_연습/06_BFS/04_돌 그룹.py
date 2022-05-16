# https://www.acmicpc.net/problem/12886
import collections
import itertools

stones = list(map(int, input().split()))
total = sum(stones)
visited = collections.defaultdict(bool)

def bfs():
    q = collections.deque()
    q.append(stones)
    # defaultdict hashing은 tuple
    visited[tuple(stones)] = True
    while q:
        a, b, c = q.popleft()
        if a==b==c:
            return 1

        for x, y in itertools.combinations([a, b, c], 2):
            if x == y:
                continue
            elif x < y:
                y -= x
                x += x
            elif x > y:
                x -= y
                y += y
            z = total - x - y

            if not visited[(x, y, z)]:
                visited[(x, y, z)] = True
                q.append([x, y, z])
    return 0
print(bfs())