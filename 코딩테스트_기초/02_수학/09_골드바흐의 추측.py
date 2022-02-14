# https://www.acmicpc.net/problem/6588

MAX = 1000000
check = [False] * (MAX + 1)
check[0] = check[1] = True
i = 2
prime = []
# 어떤 수가 소수인지 아닌지 판별하기 위해 루트 n방법을 사용할 필요는 없다
# 에라토스테네스의 체의 결과에서 지워지지 않았으면 소수, 안지워졌으면 소수가 아니기 때문
while i * i <= MAX:
    # 해당 수가 소수라면
    if not check[i]:
        j = 2
        prime.append(i)
        while i * j <= MAX:
            check[i * j] = True
            j += 1
    i += 1

prime = prime[1:]

while True:
    n = int(input())
    if n == 0:
        break
    for p in prime:
        # n - p가 소수이면
        if not check[n - p]:
            print("{} = {} + {}".format(n, p, n - p))
            break