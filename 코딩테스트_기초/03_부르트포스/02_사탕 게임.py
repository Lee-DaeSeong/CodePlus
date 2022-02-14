# https://www.acmicpc.net/problem/3085
import sys

input = sys.stdin.readline
n = int(input())
maps = [list(input().strip()) for _ in range(n)]

# 4방 탐색이 아니라
# 아래, 오른쪽만 탐색해도 모든 칸 탐색 가능
dx = [1, 0]
dy = [0, 1]

ans = 0


# n^2 방법
def count():
    ret = 1
    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if maps[i][j] == maps[i][j - 1]:
                cnt += 1
            else:
                cnt = 1

            ret = max(ret, cnt)
        cnt = 1
        for j in range(1, n):
            if maps[j][i] == maps[j - 1][i]:
                cnt += 1
            else:
                cnt = 1
            ret = max(ret, cnt)
    return ret

# 3n 방법
def count2(a, start_row, end_row, start_col, end_col):
    n = len(a)
    ans = 1

    # 행 검사
    for i in range(start_row, end_row+1):
        cnt = 1
        for j in range(1, n):
            # 이전 색이랑 같으면 +1
            if a[i][j] == a[i][j-1]:
                cnt += 1
            # 다르면 cnt = 1
            else:
                cnt = 1
            if ans < cnt:
                ans = cnt

    # 열 검사
    for i in range(start_col, end_col+1):
        cnt = 1
        for j in range(1, n):
            if a[j][i] == a[j-1][i]:
                cnt += 1
            else:
                cnt = 1
            if ans < cnt:
                ans = cnt
    return ans


for i in range(n):
    for j in range(n):
        if i == j:
            continue

        for k in range(2):
            nx = i + dx[k]
            ny = j + dy[k]

            if nx < n and ny < n:

                # 아래 swap 변화 위치
                # i행, i+1행, j열
                if k == 0:
                    maps[nx][ny], maps[i][j] = maps[i][j], maps[nx][ny]
                    ans = max(ans, count2(maps, i, i+1, j, j))
                    # 원상 복구
                    maps[nx][ny], maps[i][j] = maps[i][j], maps[nx][ny]
                # 오른쪽 swap 변화 위치
                # i행, j열, j+1열
                else:
                    maps[nx][ny], maps[i][j] = maps[i][j], maps[nx][ny]
                    ans = max(ans, count2(maps, i, i, j, j+1))
                    # 원상 복구
                    maps[nx][ny], maps[i][j] = maps[i][j], maps[nx][ny]

print(ans)
