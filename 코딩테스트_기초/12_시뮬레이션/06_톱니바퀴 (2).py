# https://www.acmicpc.net/problem/15662

import collections

t=int(input())
wheel=[collections.deque(map(int, list(input()))) for _ in range(t)]
k=int(input())
commands=[]

for _ in range(k):
    a, b = map(int, input().split())
    commands.append([a-1, b])

for cmd in commands:
    cur=cmd[0]
    origin_d=cmd[1]
    prev2=wheel[cur][2]
    prev6=wheel[cur][6]
    wheel[cur].rotate(origin_d)

    d=origin_d
    for i in range(cur+1, t):
        if wheel[i][6] != prev2:
            prev2 = wheel[i][2]
            wheel[i].rotate(d*-1)
            d*=-1
        else:
            break

    d=origin_d
    for i in range(cur-1, -1, -1):
        if wheel[i][2] == prev6:
           break
        prev6 = wheel[i][6]
        d*=-1
        wheel[i].rotate(d)

ans=0
for i in wheel:
    if i[0]== 1:
        ans+=1
print(ans)