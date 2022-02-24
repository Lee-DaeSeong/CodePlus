# https://www.acmicpc.net/problem/10845

import sys
import math
import bisect
input = sys.stdin.readline
import collections
q=collections.deque()
n=int(input())
for _ in range(n):
    query = input().rstrip().split(' ')
    if query[0] == 'push':
        q.append(query[1])
    elif query[0] == 'pop':
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif query[0] == 'size':
        print(len(q))
    elif query[0] == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif query[0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif query[0] == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)