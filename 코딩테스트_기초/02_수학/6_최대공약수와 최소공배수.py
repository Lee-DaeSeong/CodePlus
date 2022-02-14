# https://www.acmicpc.net/problem/2609

# 최대 공약수 (유클리드 호제법)
def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

a, b = map(int, input().split())
# 최대 공약수 = g
g = gcd(a, b)
print(g)
# ex) 세 수의 최대 공약수
# gcd(a, b, c) -> gcd(gcd(a, b), c)

# 최소 공배수 = l = a*b//g
print(a * b // g)
