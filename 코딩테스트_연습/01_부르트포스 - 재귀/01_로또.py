# https://www.acmicpc.net/problem/6603

import collections
import sys
input = sys.stdin.readline
import itertools

def dfs(nums, arr, idx, cnt):

    if cnt == 6:
        print(*arr)
        return
    if idx == len(nums):
        return
    dfs(nums, arr + [nums[idx]], idx+1, cnt+1)
    dfs(nums, arr, idx+1, cnt)

k=1
while k!=0:
    nums=list(map(int, input().rstrip().split()))
    k=nums.pop(0)

    dfs(nums, [], 0, 0)
    print()
