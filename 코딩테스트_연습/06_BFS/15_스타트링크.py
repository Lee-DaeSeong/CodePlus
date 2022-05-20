# https://www.acmicpc.net/problem/5014
import collections

f, s, g, u, d = map(int, input().split())

visited = [-1] * 1000001
visited[s] = 0
dx = [u, -d]
q = collections.deque()
q.append(s)


def bfs():
    while q:
        cur = q.popleft()
        if cur == g:
            return visited[cur]
        for i in [u, -d]:
            move = cur + i

            if 0 < move <= f and visited[move] == -1:
                q.append(move)
                visited[move] = visited[cur] + 1
    return "use the stairs"


print(bfs())
