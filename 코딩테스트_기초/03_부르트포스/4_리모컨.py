# https://www.acmicpc.net/problem/1107


target=int(input())
n=int(input())
# n==0이면 숫자 패드 입력이 안들어 옴
if n == 0:
    nums=[]
else:
    nums=list(map(int, input().split()))

# 없는 숫자 -> False
arr=[True]*10
for n in nums:
    arr[n] = False

# 시작 숫자가 100, 번호를 안누르고 +/- 만 눌러서 답을 찾는 경우를 초기값으로 둠
ans=abs(100 - target)

# 숫자의 각 자릿수를 확인하는 하고, 숫자의 길이를 리턴
def check(n):
    if n == 0:
        if arr[0]:
            return 1
        else:
            return 0
    ret=0
    while n > 0:
        if not arr[n%10]:
            return 0
        ret+=1
        n//=10
    return ret

for i in range(1000000):
    cnt=check(i)

    if cnt > 0:
        ans=min(ans, cnt+abs(target-i))
print(ans)