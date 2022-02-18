# https://www.acmicpc.net/problem/10971
import itertools
import math
import sys
input = sys.stdin.readline
n=int(input())
w=[list(map(int, input().split())) for _ in range(n)]
ans=math.inf
for i in itertools.permutations(range(n)):
    temp=0
    flag=True
    for j in range(n-1):
        if w[i[j]][i[j+1]]==0 or temp > ans:
            flag=False
            break
        temp+=w[i[j]][i[j+1]]

    if flag and w[i[-1]][i[0]] != 0:
        temp += w[i[-1]][i[0]]
        ans=min(ans, temp)

print(ans)