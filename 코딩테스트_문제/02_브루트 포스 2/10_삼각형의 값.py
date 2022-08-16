# https://www.acmicpc.net/problem/4902
import math

tc = 1
while True:
    temp = input()
    if temp == '0':
        break
    n = int(temp[0])
    arr = [[0] * (2 * n) for _ in range(n + 1)]
    pre_sum = [[0] * (2 * n) for _ in range(n + 1)]
    temp = list(map(int, temp.split()))
    idx = 1
    for i in range(1, n + 1):
        for j in range(1, 2 * i):
            arr[i][j] = temp[idx]
            pre_sum[i][j] = arr[i][j] + pre_sum[i][j - 1]
            idx += 1

    ans = -math.inf
    for i in range(1, n + 1):
        for j in range(1, 2 * i, 2):
            temp = 0
            for k in range(n - i + 1):
                temp += pre_sum[i + k][j + 2 * k] - pre_sum[i + k][j - 1]
                ans = max(ans, temp)

    for i in range(n, 0, -1):
        for j in range(2, 2 * i, 2):
            temp = 0
            for k in range(n + 1):
                if (j-2*k-1<0 or j>=2*(i-k)):
                    break
                temp += pre_sum[i - k][j] - pre_sum[i - k][j - 2 * k - 1]
                ans = max(ans, temp)

    print("{}. {}".format(tc, ans))
    tc += 1
