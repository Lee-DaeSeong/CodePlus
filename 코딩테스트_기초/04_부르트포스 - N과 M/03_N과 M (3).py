# https://www.acmicpc.net/problem/15651

import itertools

n, m = map(int, input().split())

# 1부터 N까지 자연수 중에서 중복 포함 M개를 고른 수열
# 중복 순열 product (중복 o, 순서 0)
# for i in itertools.product(range(1, n+1), repeat=m):
#     print(*i)

c=[False] * (n+1)
a=[0]*m

def go(idx, n, m):
    if idx == m:
        print(*a)
        return

    for i in range(1, n+1):
        # 해당 수 선택 됨
        # if c[i]:
        #     continue  # 중복 허용

        # c[i] = True     # 사용 o
        a[idx] = i
        go(idx+1, n, m) # 재귀 호출
        # c[i] = False    # 사용 x

go(0, n, m)