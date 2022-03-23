# https://www.acmicpc.net/problem/16967

h,w,x,y = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(h+x)]
for i in range(h):
    for j in range(w):
        a[i+x][j+y] -= a[i][j]
for i in range(h):
    print(*a[i][:w])
