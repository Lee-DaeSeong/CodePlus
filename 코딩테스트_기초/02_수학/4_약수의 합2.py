# https://www.acmicpc.net/problem/17427


n = int(input())
ans = 0
# 약수를 전부 구하는 것이 아닌
# i의 약수 개수 * i를 구함
# ex) N 이하의 자연수 중에서 1을 약수로 갖는 수의 개수 -> floor(N/1)
# 2를 약수로 갖눈 수의 개수 -> floor(N/2)
for i in range(1, n + 1):
    ans += int(n // i) * i
print(ans)
