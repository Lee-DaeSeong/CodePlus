# https://www.acmicpc.net/problem/1929

"""
    에라토스테네스의 체 - 1 ~ N 까지의 모든 소수 찾기

    1. 2 ~ N 까지 모든 수 생성
    2. 아직 지위지지 않은 수 중에서 가장 작은 수 찾기
    3. 그 수는 소수이고, 그 수의 배수를 모두 지움

    어떤 수의 제곱 부터 값들을 지우면 됨
    그 수의 제곱 보다 작은 수들은 이미 지워져 있음
"""


n, m = map(int, input().split())
check=[False] * (m+1)
check[0] = check[1] = True
i=2

# 사실 어떤 수가 소수인지 아닌지 판별하기 위해 루트 n방법을 사용할 필요는 없다
# 에라토스테네스의 체의 결과에서 지워지지 않았으면 소수, 안지워졌으면 소수가 아니기 때문
while i*i<=m:
    # 해당 수가 소수라면
    if not check[i]:
        # i의 배수 지워 주기
        j=2
        while i*j <=m:
            check[i*j] = True
            j+=1
    i+=1
ans=[]
for i in range(n, m+1):
    if not check[i]:
        ans.append(i)
print('\n'.join(map(str, ans)))