# https://www.acmicpc.net/problem/14889
import itertools
import math

n=int(input())
ability=[list(map(int, input().split())) for _ in range(n)]
ans=math.inf

def dfs(idx, first, second):
    if len(first) == n//2 and len(second) == n//2:
        global ans
        f=0
        s=0

        for i in range(n//2):
            for j in range(n//2):
                if i!=j:
                    f += ability[first[i]][first[j]]
                    s += ability[second[i]][second[j]]

        ans=min(ans, abs(f-s))
        return
    if len(first) > n//2 or len(second) > n//2:
        return

    # first + [idx]를 넘겨주어
    # first 값에는 변화가 없기 때문에
    # pop()과정이 없어도 됨
    dfs(idx+1, first+[idx], second)
    dfs(idx+1, first, second + [idx])


dfs(0, [], [])
print(ans)