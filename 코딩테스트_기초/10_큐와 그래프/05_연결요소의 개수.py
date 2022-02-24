# https://www.acmicpc.net/problem/11724

'''
    이분 그래프
    그래프를 A와 B로 나눌 수 있음
    A에 포함되어 있는 정점 끼리 연결된 간선 x
    B에 포함되어 있는 정점 끼리 연결된 간선 x
    모든 간선의 한 끝 점은 A에 다른 끝 점은 B에
'''
import collections
import sys
sys=sys.stdin.readline
n, m = map(int, input().split())

graph=[[0] * (n+1) for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x][y]=1
    graph[y][x]=1
def bfs(v):
    visited[v] = True
    q=collections.deque()
    q.append(v)
    while q:
        cur = q.popleft()

        for i in range(1, n+1):
            if not visited[i] and graph[cur][i] == 1:
                q.append(i)
                visited[i] = True

visited = [False] * (n+1)

ans=0
for i in range(1, n+1):
    if not visited[i]:
        ans+=1
        bfs(i)
print(ans)