# https://www.acmicpc.net/problem/14890

n, l = map(int, input().split())

maps=[list(map(int, input().split())) for _ in range(n)]

def check(maps):

    block=[[False] * n for _ in range(n)]
    for i in range(n):
        j=0
        flag=True
        while j < n-1:
            if maps[i][j] == maps[i][j+1]:
                j+=1
                continue

            elif maps[i][j] - maps[i][j+1] == 1: # 높 -> 낮
                if maps[i][j+1:j+1+l].count(maps[i][j+1]) == l:

                    # block 사용 중
                    block[i][j+1:j+1+l]=[True]*l
                    j+=l
                else:
                    flag = False
                    break
            elif maps[i][j] - maps[i][j+1] == -1: # 낮 -> 높
                # block이 겹치지 않을 때 block을 놓을 수 있음
                if maps[i][j-l+1:j+1].count(maps[i][j]) == l and True not in block[i][j-l+1:j+1]:
                    j+=1
                else:
                    flag = False
                    break
            else:
                flag = False
                break
        if flag:
            global ans
            ans+=1

ans=0
check(maps)
# 2차원 행렬 transpose
check(list(zip(*maps)))
print(ans)