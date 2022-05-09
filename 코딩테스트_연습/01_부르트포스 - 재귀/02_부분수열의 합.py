# https://www.acmicpc.net/problem/1182

import sys
import collections


def dfs(idx, sum):
    global ans

    # 부분집합 -> 모든 경우를 살펴보아야 함
    if idx == n:
        if sum == target:
            ans += 1
        return

    dfs(idx + 1, sum + nums[idx])
    dfs(idx + 1, sum)


n, target = map(int, input().split())
nums = list(map(int, sys.stdin.readline().rstrip().split()))

ans = 0
dfs(0, 0)

# target이 0일 때 공집합 예외 처리
if target == 0:
    ans -= 1
print(ans)
