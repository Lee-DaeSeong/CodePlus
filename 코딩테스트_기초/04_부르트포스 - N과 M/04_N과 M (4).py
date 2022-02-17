# https://www.acmicpc.net/problem/15652

import itertools
import sys

n, m = map(int, input().split())

# 1부터 N까지 자연수 중에서 중복 포함 M개를 고른 수열
# 같은 수 여러 번 골라도 된다 (중복)
# 고른 수열은 오름차순
# 중복 조합 combinations_with_replacement (중복 o, 순서 x)
# for i in itertools.combinations_with_replacement(range(1, n+1), r=m):
#     print(*i)

a=[0]*m

c = [False] * (n+1)
def go(index, start, n, m):
    if index == m:
        for i in range(m):
            sys.stdout.write(str(a[i])+' ')
        sys.stdout.write('\n')
        return
    for i in range(start, n+1):
        # c[i] = True
        a[index] = i
        go(index+1, i, n, m)
        # c[i] = False

go(0,1,n,m)