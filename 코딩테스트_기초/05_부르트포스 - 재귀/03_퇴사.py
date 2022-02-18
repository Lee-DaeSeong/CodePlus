# https://www.acmicpc.net/problem/14501
n=int(input())
schedule=[list(map(int, input().split())) for _ in range(n)]
ans=0

def dfs(day, price):
    # n+1일에 퇴사
    if day == n+1:
        global ans
        ans = max(ans, price)
        return
    # n+1일이 넘으면 조건 x
    if day > n+1:
        return

    dfs(day+schedule[day-1][0], price+schedule[day-1][1])
    # 선택 x, day + 1 -> 다음 날
    dfs(day+1, price)

dfs(1, 0)
print(ans)