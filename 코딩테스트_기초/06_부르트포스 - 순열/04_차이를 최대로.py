# https://www.acmicpc.net/problem/10819
import math
n=int(input())
arr=list(map(int, input().split()))
a=[0] * n
c=[False] * (n+1)
ans=-math.inf
def dfs(idx):
    if idx == n:
        global ans
        temp=0
        for i in range(n-1):
            temp += abs(a[i] - a[i+1])
        ans = max(ans, temp)

    for i in range(n):
        if c[i]:
            continue
        a[idx]=arr[i]
        c[i]=True
        dfs(idx+1)
        c[i]=False
dfs(0)
print(ans)