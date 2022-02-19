# https://www.acmicpc.net/problem/14391

# a[i][j] == a[i*m+j]
n, m = map(int,input().split())
a = [list(map(int,list(input()))) for _ in range(n)]
ans = 0
for s in range(1<<(n*m)):
    sum = 0
    print(s, bin(s))
    # 가로 합 계산
    for i in range(n):
        cur = 0
        for j in range(m):
            # k == 이차원 배열을 일렬로 늘렸을때의 인덱스가 어디인지 의미
            k = i*m+j
            # 가로일 때 
            if (s&(1<<k)) == 0:
                cur = cur * 10 + a[i][j]    # 3 (0 * 10 + 3)
                                            # 35 (3 * 10 + 5)
                                            # 352 (35 * 10 + 2)
            # 세로일 때
            else:
                sum += cur
                cur = 0
        # 가로로 끝나는 경우가 있기 때문에 sum에 cur을 더해줌
        sum += cur

    # 세로 계산
    for j in range(m):
        cur = 0
        for i in range(n):
            k = i*m+j
            # 세로일 때
            if (s&(1<<k)) != 0:
                cur = cur * 10 + a[i][j]
            # 가로일 때
            else:
                sum += cur
                cur = 0
        sum += cur
    ans = max(ans, sum)
print(ans)
