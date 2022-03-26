# https://www.acmicpc.net/problem/1182

import sys
import collections


def dfs(idx, sum):
    global ans

    if idx == len(nums):
        return

    if sum + nums[idx] == target:
        ans += 1

    dfs(idx + 1, sum + nums[idx])
    dfs(idx + 1, sum)


n, target = map(int, input().split())
nums = list(map(int, sys.stdin.readline().rstrip().split()))
ans = 0
dfs(0, 0)
print(ans)
