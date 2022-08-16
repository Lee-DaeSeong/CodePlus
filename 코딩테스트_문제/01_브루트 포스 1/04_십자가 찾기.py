# https://www.acmicpc.net/problem/16924

n, m = map(int, input().split())
maps = [list(input()) for _ in range(n)]

visited = [[False] * m for _ in range(n)]
ans = []
for i in range(n):
    for j in range(m):
        if maps[i][j] == '*':
            temp = 0
            k = 1
            while True:
                if 0 <= i + k < n and 0 <= i - k < n and 0 <= j + k < m and 0 <= j - k < m \
                        and maps[i + k][j] == '*' and maps[i - k][j] == '*' \
                        and maps[i][j + k] == '*' and maps[i][j - k] == '*':
                    temp = k
                else:
                    k = 0
                    break
                k += 1

            if temp:
                ans.append([i + 1, j + 1, temp])
                for l in range(temp + 1):
                    visited[i + l][j] = True
                    visited[i - l][j] = True
                    visited[i][j + l] = True
                    visited[i][j - l] = True

for i in range(n):
    for j in range(m):
        if maps[i][j] == '*' and not visited[i][j]:
            print(-1)
            exit()

print(len(ans))
for a in ans:
    print(*a)
