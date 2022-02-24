# https://www.acmicpc.net/problem/1463

n = int(input())
d = [0] * (10**6 + 1)
d[1] = 0
for i in range(2, n + 1):

    # d[i-1]은 모든 i가 가능한 연산이기에
    # d[i-1]부터 계산
    d[i] = d[i - 1] + 1

    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
print(d[n])