# https://www.acmicpc.net/problem/16198

import itertools

n = int(input())
nums = list(map(int, input().split()))
ans = 0


def dfs(point, arr):
    if len(arr) == 2:
        global ans
        ans = max(ans, point)
        return

    for i in range(1, len(arr) - 1):
        temp = point + (arr[i - 1] * arr[i + 1])
        dfs(temp, arr[:i] + arr[i + 1:])


dfs(0, nums)

print(ans)
