# https://www.acmicpc.net/problem/14888
import math

n = int(input())
nums = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
min_ans = math.inf
max_ans = -(math.inf)

def dfs(i, now, a, s, m, d):
    global min_ans, max_ans

    if i == n:
        min_ans = min(min_ans, now)
        max_ans = max(max_ans, now)
    else:
        if a > 0:
            dfs(i + 1, now + nums[i], a - 1, s, m, d)
        if s > 0:
            dfs(i + 1, now - nums[i], a, s-1, m, d)
        if m > 0:
            dfs(i + 1, now * nums[i], a, s, m-1, d)
        if d > 0:
            dfs(i + 1, int(now / nums[i]), a, s, m, d-1)


dfs(1, nums[0], add, sub, mul, div)
print(max_ans)
print(min_ans)
