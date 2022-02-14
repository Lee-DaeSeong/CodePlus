# https://www.acmicpc.net/problem/10430

A, B, C = input().split()
A = int(A)
B = int(B)
C = int(C)
# 아래 두개 식 동일
print((A + B) % C)
print(((A % C) + (B % C)) % C)
# 아래 두개 식 동일
print((A * B) % C)
print(((A % C) * (B % C)) % C)
