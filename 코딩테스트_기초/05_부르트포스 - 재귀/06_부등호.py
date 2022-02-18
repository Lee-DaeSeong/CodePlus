# https://www.acmicpc.net/problem/2529

import itertools

n=int(input())
ops=list(input().split())

def valid(x, y, op):
    if op == '>':
        if int(x)>int(y):
            return True
    elif op == '<':
        if int(x)<int(y):
            return True
    return False
ans=[]
def dfs(idx, num):
    if idx==(n+1):
        global ans
        ans.append(num)
        return

    for i in range(10):
        if check[i]:
            continue

        # idx == 0일 경우 비교 대상이 없기에 i 사용
        if idx == 0 or valid(num[idx-1], i, ops[idx-1]):
            check[i]=True
            dfs(idx+1, num+str(i))
            check[i]=False

check=[False] * 10
dfs(0, '')
ans.sort()
print(ans[-1])
print(ans[0])