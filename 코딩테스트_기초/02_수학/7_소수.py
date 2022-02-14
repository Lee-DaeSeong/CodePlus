# https://www.acmicpc.net/problem/1978

# 시간 복잡도 sqrt(n)
def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

int(input())
arr = list(map(int, input().split()))
print(sum([is_prime(x) for x in arr]))