# https://www.acmicpc.net/problem/14888
import math

n = int(input())
nums = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
min_ans = math.inf
max_ans = -(math.inf)

def dfs(i, now):
    global min_ans, max_ans, add, sub, mul, div

    if i == n:
        min_ans = min(min_ans, now)
        max_ans = max(max_ans, now)
    else:
        if add > 0:
            add -= 1
            dfs(i + 1, now + nums[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i + 1, now - nums[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, now * nums[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i + 1, int(now / nums[i]))
            div += 1


dfs(1, nums[0])
print(max_ans)
print(min_ans)
