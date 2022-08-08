# https://www.acmicpc.net/workbook/view/9390
import collections

a, b = input().split()
a = list(map(int, str(a)))
b = int(b)

def dfs(idx, num):
    if idx == len(a):
        if num < b:
            global ans
            ans = max(ans, num)
        return

    for i in range(len(a)):
        if idx == 0 and a[i] == 0:
            continue

        if not check[i]:
            check[i] = True
            dfs(idx + 1, num * 10 + a[i])
            check[i] = False


ans = -1
check = [False] * len(a)
dfs(0, 0)
print(ans)