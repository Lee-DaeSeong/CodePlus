# https://www.acmicpc.net/problem/20061

def simulate(board, col, what):
    # what = type (C++, Java)
    # what = 1 1x1, 2 = garo (col, col+1), 3 = sero
    ans = 0
    max_row = -1
    for i in range(len(board)):
        if board[i][col] == 0:
            max_row = i
        else:
            break
    if what == 2:
        max_row_2 = -1
        for i in range(len(board)):
            if board[i][col+1] == 0:
                max_row_2 = i
            else:
                break
        max_row = min(max_row, max_row_2)
    board[max_row][col] = 1
    if what == 2:
        board[max_row][col+1] = 1
    if what == 3:
        board[max_row-1][col] = 1
    deleted_row = -1
    for i in range(len(board)):
        ok = True # ok = all (C++, Java)
        for j in range(len(board[i])):
            if board[i][j] == 0:
                ok = False
        if ok:
            if deleted_row < i:
                deleted_row = i
            ans += 1
            for j in range(len(board[i])):
                board[i][j] = 0
    if ans > 0:
        for i in range(deleted_row, -1, -1):
            for j in range(len(board[i])):
                board[i][j] = 0
                if i - ans >= 0:
                    board[i][j] = board[i-ans][j]
    cnt = 0
    for i in range(0, 2):
        exists = False
        for j in range(len(board[i])):
            if board[i][j] != 0:
                exists = True
        if exists:
            cnt += 1
    if cnt > 0:
        bn = len(board)
        for i in range(bn-1, -1, -1):
            for j in range(len(board[i])):
                board[i][j] = 0
                if i - cnt >= 0:
                    board[i][j] = board[i-cnt][j];

    return ans

n = int(input())
ans = 0
green = [[0]*4 for _ in range(6)]
blue = [[0]*4 for _ in range(6)]
for _ in range(n):
    t,x,y = map(int,input().split())
    if t == 1:
        ans += simulate(green, y, 1)
    elif t == 2:
        ans += simulate(green, y, 2)
    elif t == 3:
        ans += simulate(green, y, 3)
    if t == 1:
        ans += simulate(blue, x, 1)
    elif t == 2:
        ans += simulate(blue, x, 3)
    elif t == 3:
        ans += simulate(blue, x, 2)

print(ans)
cnt = 0
for i in range(len(green)):
    for j in range(len(green[i])):
        if green[i][j] > 0:
            cnt += 1
for i in range(len(blue)):
    for j in range(len(blue[i])):
        if blue[i][j] > 0:
            cnt += 1
print(cnt)
