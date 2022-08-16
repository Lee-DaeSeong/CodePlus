# https://www.acmicpc.net/problem/16638
import math

n = int(input())
calc = list(input())
op_cnt = (n + 1) // 2 - 1
ans = -math.inf

for s in range(1 << op_cnt):
    flag = True

    # 괄호가 연속으로 있는 경우 찾기
    for i in range(op_cnt - 1):
        if (s & (1 << i)) > 0 and (s & (1 << (i + 1))) > 0:
            flag = False

    if not flag:
        continue

    temp = calc[:]
    for i in range(op_cnt):
        if s & (1 << i) > 0:
            k = 2 * i + 1
            temp[k - 1] = '(' + temp[k - 1]
            temp[k + 1] = temp[k + 1] + ')'
    ans = max(ans, eval(''.join(temp)))
print(ans)
