# https://www.acmicpc.net/problem/16953
import collections

a, b = map(int, input().split())

q = collections.deque()
q.append([a, 1])
ans = -1
while q:
    x, cnt = q.popleft()
    if x == b:
        ans = cnt
        break
    if x > b:
        continue
    for i in [x * 2, x * 10 + 1]:
        q.append([i, cnt + 1])
print(ans)