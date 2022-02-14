# https://www.acmicpc.net/problem/17425

# test case가 여러개인 문제는 중복 사용 되는 값들을 구해두고 재사용

MAX = 1000000
d = [1] * (MAX + 1)
s = [0] * (MAX + 1)

# D를 모두 구함
# i의 배수들의 값을 더 해줌
for i in range(2, MAX + 1):
    j = 1
    while i * j <= MAX:
        d[i * j] += i
        j += 1

# d[i] = f(i)
# s[i] = g(i)
# s[i] = d[1] + d[2] + ... + d[i]
# s[i] = s[i-1] + d[i]
for i in range(1, MAX + 1):
    s[i] = s[i - 1] + d[i]

# 출력 속도
# print() 여러번 >>> 출력 값 묶어서 print() 1번
t = int(input())
ans = []
for i in range(t):
    ans.append(s[int(input())])
print('\n'.join(map(str, ans)) + '\n')
