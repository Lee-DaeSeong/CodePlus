# https://www.acmicpc.net/problem/14499

n, m, x, y, k = map(int, input().split())

dice=[0] * 7

maps=[list(map(int, input().split())) for _ in range(n)]
cmds=list(map(int, input().split()))

# 동 서 북 남
dx=[0, 0, -1, 1]
dy=[1, -1, 0, 0]

def turn(cmd):
    if cmd==1: # 동
        dice[1], dice[3], dice[6], dice[4] = dice[4], dice[1], dice[3], dice[6]
    if cmd==2: # 서
        dice[1], dice[3], dice[6], dice[4] = dice[3], dice[6], dice[4], dice[1]
    if cmd==3: # 북
        dice[1], dice[2], dice[6], dice[5] = dice[5], dice[1], dice[2], dice[6]
    if cmd==4: # 남
        dice[1], dice[2], dice[6], dice[5] = dice[2], dice[6], dice[5], dice[1]

for cmd in cmds:
    nx = x + dx[cmd-1]
    ny = y + dy[cmd-1]

    if 0<=nx<n and 0<=ny<m:
        turn(cmd)

        if maps[nx][ny] == 0:
            maps[nx][ny] = dice[6]
        else:
            dice[6] = maps[nx][ny]
            maps[nx][ny] = 0

        print(dice[1])
        x, y = nx, ny