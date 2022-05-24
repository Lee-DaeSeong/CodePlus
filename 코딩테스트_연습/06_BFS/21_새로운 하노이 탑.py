# https://www.acmicpc.net/problem/12906

import collections

q = collections.deque()
start = []
for i in range(3):
    temp = input().split()
    cnt = int(temp[0])
    if cnt > 0:
        start.append(temp[1])
    else:
        start.append('')

cnt = [0, 0, 0]
for i in range(3):
    for char in start[i]:
        cnt[ord(char)-ord('A')] += 1

q = collections.deque()
q.append(tuple(start))
visited = dict()
visited[tuple(start)] = 0
while q:
    x = q.popleft()
    for i in range(3):
        for j in range(3):
            if i != j and len(x[i]) > 0:
                y = list(x[:])
                y[j] = y[j] + x[i][-1]
                y[i] = y[i][:-1]
                y = tuple(y)
                if y not in visited:
                    visited[y] = visited[x] + 1
                    q.append(y)

ans = [''] * 3
for i in range(3):
    for j in range(cnt[i]):
        ans[i] += chr(ord('A')+i)

print(visited[tuple(ans)])