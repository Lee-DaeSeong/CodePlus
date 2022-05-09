# https://www.acmicpc.net/problem/1062

n, k = map(int, input().split())

words = [set(input()) for _ in range(n)]

learn = [False] * 26

for i in ['a', 'n', 't', 'i', 'c']:
    learn[ord(i) - 97] = True

def dfs(idx, cnt):
    if cnt == k - 5:
        cur = 0
        for word in words:
            check=True
            for w in word:
                if learn[ord(w) - 97] == False:
                    check=False
                    break
            if check:
                cur+=1
        global ans
        ans = max(ans, cur)

    for i in range(idx, 26):
        if not learn[i]:
            learn[i] = True
            dfs(i, cnt+1)
            learn[i] = False

ans=0
dfs(0, 0)
print(ans)
