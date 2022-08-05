# https://www.acmicpc.net/problem/17088
import math

n = int(input())
nums = list(map(int, input().split()))

if n == 1:
    print(0)
    exit()

ans = math.inf
for d1 in [-1, 0, 1]:
    for d2 in [-1, 0, 1]:
        cnt = 0
        if d1 != 0:
            cnt += 1
        if d2 != 0:
            cnt += 1

        n0 = nums[0] + d1
        diff = nums[1] + d2 - n0
        an = n0 + diff
        flag = True
        for i in range(2, n):
            an += diff
            if nums[i] == an:
                continue
            elif nums[i] == an - 1:
                cnt += 1
            elif nums[i] == an + 1:
                cnt += 1
            else:
                flag = False
                break

        if flag:
            ans = min(ans, cnt)

if ans == math.inf:
    ans = -1
print(ans)
