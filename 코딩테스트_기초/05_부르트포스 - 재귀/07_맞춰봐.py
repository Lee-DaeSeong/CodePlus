# https://www.acmicpc.net/problem/1248

n = int(input())
s = input()
sign = [[0] * n for _ in range(n)]

ans = [0] * n
cnt = 0
for i in range(n):
    for j in range(i, n):
        if s[cnt] == '0':
            sign[i][j] = 0
        elif s[cnt] == '+':
            sign[i][j] = 1
        elif s[cnt] == '-':
            sign[i][j] = -1
        cnt += 1


def check(index):
    s = 0
    # 현재 인덱스 부터 계산하기 위해 idx -> 0까지 계산
    # 0 -> idx 까지 계산 하려면
    for i in range(index, -1, -1):
        s += ans[i]
        if sign[i][index] == 0:
            if s != 0:
                return False
        elif sign[i][index] < 0:
            if s >= 0:
                return False
        elif sign[i][index] > 0:
            if s <= 0:
                return False
    return True


def dfs(idx):
    if idx == n:
        return True

    if sign[idx][idx] == 0:
        ans[idx] = 0
        return check(idx) and dfs(idx + 1)

    for i in range(1, 11):
        ans[idx] = i * sign[idx][idx]
        if check(idx) and dfs(idx + 1):
            return True

    return False


dfs(0)
print(*ans)
