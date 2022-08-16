# https://www.acmicpc.net/problem/16987

n = int(input())
power = [0] * n
weight = [0] * n

for i in range(n):
    a, b = map(int, input().split())
    power[i] = a
    weight[i] = b


def dfs(idx):
    if idx == n:
        cnt = 0
        for i in range(n):
            if power[i] <= 0:
                cnt += 1
        global ans
        ans = max(ans, cnt)
        return

    if power[idx] <= 0:
        return dfs(idx + 1)

    flag = True
    for i in range(n):
        if idx == i:
            continue
        if power[i] > 0:
            flag = False
            power[i] -= weight[idx]
            power[idx] -= weight[i]
            dfs(idx + 1)
            power[i] += weight[idx]
            power[idx] += weight[i]
    if flag:
        dfs(idx + 1)


ans = 0
dfs(0)
print(ans)
