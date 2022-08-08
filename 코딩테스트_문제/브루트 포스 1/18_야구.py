# https://www.acmicpc.net/problem/17281
import itertools

n = int(input())
innings = [list(map(int, input().split())) for _ in range(n)]
player = [0] * 9
visited = [0] * 9


def solve():

    cur = 0
    score = 0
    for i in range(n):
        inning = innings[i]
        b1 = 0
        b2 = 0
        b3 = 0
        out = 0

        while out < 3:
            res = inning[player[cur]]
            if res == 0:
                out += 1

            if res == 1:
                score += b3
                b3 = b2
                b2 = b1
                b1 = 1

            if res == 2:
                score += b3 + b2
                b3 = b1
                b2 = 1
                b1 = 0

            if res == 3:
                score += b3 + b2 + b1
                b3 = 1
                b2 = 0
                b1 = 0

            if res == 4:
                score += b3 + b2 + b1 + 1
                b3 = 0
                b2 = 0
                b1 = 0

            cur += 1

            if cur == 9:
                cur = 0

    global ans
    ans = max(score, ans)

def dfs(idx):
    if idx == 9:
        solve()
        return

    if idx == 3:
        player[3] = 0
        dfs(idx + 1)

    for i in range(9):
        if not visited[i]:
            visited[i] = True
            player[idx] = i
            dfs(idx + 1)
            visited[i] = False
            player[idx] = 0

ans = 0
visited[0] = True
dfs(0)
print(ans)