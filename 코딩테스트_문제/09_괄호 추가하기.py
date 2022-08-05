# https://www.acmicpc.net/problem/16637
import math

n = int(input())
calc = list(input())

nums, op = [], []

for c in calc:
    if c.isdigit():
        nums.append(c)
    else:
        op.append(c)


# cur <- 현재까지 계산 결과
def dfs(idx, cur):
    if idx == len(op):
        global ans
        ans = max(ans, int(cur))
        return

    # (1 + 2) * 3
    first = str(eval(cur + op[idx] + nums[idx + 1]))
    dfs(idx + 1, first)

    if idx + 1 < len(op):
        # 1 + (2 * 3)
        second = str(eval(cur + op[idx] + str(eval(nums[idx + 1] + op[idx + 1] + nums[idx + 2]))))
        dfs(idx + 2, second)


ans = -math.inf
dfs(0, nums[0])
print(ans)
