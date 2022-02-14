# https://www.acmicpc.net/problem/15651

import itertools

n, m = map(int, input().split())

# 1부터 N까지 자연수 중에서 중복 포함 M개를 고른 수열
# 중복 순열 product (중복 o, 순서 0)
for i in itertools.product(range(1, n+1), repeat=m):
    print(*i)