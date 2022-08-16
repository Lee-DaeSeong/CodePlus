# https://www.acmicpc.net/problem/16922
import collections

n = int(input())

visited = collections.defaultdict(int)

for i in range(n + 1):
    for j in range(n + 1 - i):
        for k in range(n + 1 - i - j):
            l = n - i - j - k
            visited[i + 5 * j + 10 * k + 50 * l] = True

print(len(visited))
