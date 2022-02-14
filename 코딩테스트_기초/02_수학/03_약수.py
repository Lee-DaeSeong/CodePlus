# https://www.acmicpc.net/problem/1037

int(input())
data = list(map(int, input().split()))
# 진짜 약수 = 1과 N이 아님
# 가작 작은 수 * 가장 큰 수 = N
print(min(data) * max(data))
