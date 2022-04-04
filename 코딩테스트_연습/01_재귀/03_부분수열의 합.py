# https://www.acmicpc.net/problem/14225
import math
import sys
import collections

n = int(input())
nums = list(map(int, sys.stdin.readline().rstrip().split()))
c = [False] * 2000000
c[0] = True


def dfs(idx, sum):
    if idx == n:
        c[sum] = True
        return

    dfs(idx + 1, sum + nums[idx])
    dfs(idx + 1, sum)

dfs(0, 0)
print(c.index(False))
