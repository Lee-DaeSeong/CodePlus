# https://www.acmicpc.net/problem/1963
import collections

prime = [True] * 10001

for i in range(2, 10001):
    if prime[i] == True:
        for j in range(i*i, 10001, i):
            prime[j] = False

def change(num, idx, digit):
    if idx == 0 and digit == 0:
        return False
    s = list(str(num))
    s[idx] = chr(digit+ord('0'))
    return int(''.join(s))

t= int(input())
for _ in range(t):
    n, m = map(int, input().split())
    visited = [-1] * 10001
    visited[n] = 0

    q = collections.deque()
    q.append(n)

    while q:
        x = q.popleft()
        for i in range(4):
            for j in range(10):
                nxt = change(x, i, j)
                if nxt:
                    if prime[nxt] and visited[nxt] == -1:
                        q.append(nxt)
                        visited[nxt] = visited[x] + 1

    print(visited[m])