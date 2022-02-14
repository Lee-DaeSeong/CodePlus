# https://www.acmicpc.net/problem/15650

import itertools

n, m = map(int, input().split())

# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열, 고른 수열은 오름차순
# 조합 combinations (중복 x, 순서가 x)
for i in itertools.combinations(range(1, n+1), m):
    print(*i)