# https://www.acmicpc.net/problem/15661
import math

n=int(input())
ability=[list(map(int, input().split())) for _ in range(n)]
ans=math.inf

def dfs(idx, first, second):

    if idx==n and len(first) > 0 and len(second) > 0:
        global ans
        f=0
        s=0

        for i in first:
            for j in first:
                if i != j:
                    f += ability[i][j]
                    f += ability[j][i]
        for i in second:
            for j in second:
                if i != j:
                    s += ability[i][j]
                    s += ability[j][i]

        ans=min(ans, abs(f-s))
        return

    if idx == n:
        return

    # first + [idx]를 넘겨주어
    # first 값에는 변화가 없기 때문에
    # pop()과정이 없어도 됨
    dfs(idx+1, first+[idx], second)
    dfs(idx+1, first, second + [idx])


dfs(0, [], [])
print(ans//2)