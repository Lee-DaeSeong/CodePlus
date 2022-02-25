# https://www.acmicpc.net/problem/14226
import collections

target=int(input())

q=collections.deque()
q.append([1, 0])

# 이모티콘 개수, 클립보드 개수 모두 답에 영향을 끼치기 때문에
# 2차원 배열 사용

graph=[[-1] * 2000 for _ in range(2000)]
graph[1][0] = 0
if target==1:
    print(1)
    exit()

while q:
    s, c = q.popleft()

    for ns, nc in [[s, s], [s+c, c], [s-1, c]]:
        if 0 <= ns < 2000 and graph[ns][nc] == -1:
            q.append([ns, nc])
            graph[ns][nc] = graph[s][c] +1

        if ns == target:
            print(graph[ns][nc])
            exit()