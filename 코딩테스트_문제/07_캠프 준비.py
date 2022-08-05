# https://www.acmicpc.net/problem/16938
import collections

n, l, r, x = map(int, input().split())
nums = list(map(int, input().split()))
visited = collections.defaultdict(bool)

def dfs(idx, cnt, arr, arr_idx):

    if cnt >= 2:
        if l <= sum(arr) <= r and max(arr) - min(arr) >= x and not visited[tuple(arr_idx)]:
            global ans
            visited[tuple(arr_idx)] = True
            ans += 1

    if idx >= len(nums):
        return

    dfs(idx + 1, cnt + 1, arr + [nums[idx]], arr_idx + [idx])
    dfs(idx + 1, cnt, arr, arr_idx)

ans = 0
dfs(0, 0, [], [])
print(ans)