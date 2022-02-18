# https://www.acmicpc.net/problem/6603

import collections
import sys
input = sys.stdin.readline
import itertools

k=1
while k!=0:
    nums=list(map(int, input().rstrip().split()))
    k=nums.pop(0)

    for i in itertools.combinations(nums, 6):
        print(*i)
    print()
