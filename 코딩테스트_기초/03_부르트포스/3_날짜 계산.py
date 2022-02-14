# https://www.acmicpc.net/problem/1476

e, s, m = map(int, input().split())

cnt=1
a, b, c= 1, 1, 1
while True:
    if e==a and s==b and c==m:
        break

    a+=1
    b+=1
    c+=1
    # 더하고 조건 확인
    if a == 16:
        a=1
    if b == 29:
        b=1
    if c == 20:
        c=1
    cnt+=1
print(cnt)