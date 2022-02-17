# https://www.acmicpc.net/problem/15649
import itertools

n, m = map(int, input().split())

# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# 순열 permutation (중복 x, 순서 o)
# for i in itertools.permutations(range(1, n+1), m):
#     print(*i)

c=[False] * (n+1)
a=[0]*m

def go(idx, n, m):
    if idx == m:
        # print(*a)
        return

    for i in range(1, n+1):
        # 해당 수 선택 됨
        if c[i]:
            continue
        c[i] = True     # 사용 o
        a[idx] = i
        print(*a)
        go(idx+1, n, m) # 재귀 호출
        c[i] = False    # 사용 x

go(0, n, m)