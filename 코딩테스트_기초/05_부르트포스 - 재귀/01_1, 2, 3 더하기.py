# https://www.acmicpc.net/problem/9095

def dfs(x):
    if x > n:
        return
    if x == n:
        global ans
        ans+=1
        return
    dfs(x + 1)
    dfs(x + 2)
    dfs(x + 3)

for _ in range(int(input())):
    n=int(input())
    ans=0
    dfs(0)
    print(ans)