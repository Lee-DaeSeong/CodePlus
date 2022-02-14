# https://www.acmicpc.net/problem/15657

import itertools

n, m = map(int, input().split())
nums=list(map(int, input().split()))
nums.sort()
for i in itertools.combinations_with_replacement(nums, r=m):
    print(*i)