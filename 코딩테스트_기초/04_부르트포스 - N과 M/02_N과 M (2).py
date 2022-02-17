# https://www.acmicpc.net/problem/15650

import itertools

n, m = map(int, input().split())

# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열, 고른 수열은 오름차순
# 조합 combinations (중복 x, 순서가 x)
# for i in itertools.combinations(range(1, n+1), m):
#     print(*i)

a = [0] * (n)

def go(idx, selected, n, m):
    if selected == m:
        print(*a[:m])
        return
    if idx > n:
        return  # 더 이상 선택 x
    a[selected] = idx  # 선택 o
    go(idx + 1, selected + 1, n, m)
    a[selected] = 0  # 선택 x
    go(idx + 1, selected, n, m)

go(1, 0, n, m)
