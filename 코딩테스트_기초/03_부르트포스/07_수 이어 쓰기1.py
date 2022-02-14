# https://www.acmicpc.net/problem/1748


n=int(input())
ans=0
length=1
start=1
flag=False
while not flag:
    end = start*10 - 1
    if end > n:
        end = n
        flag = True
    ans += (end - start + 1) * length
    start *= 10
    length+=1
print(ans)