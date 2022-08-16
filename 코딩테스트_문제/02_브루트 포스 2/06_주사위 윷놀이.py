# https://www.acmicpc.net/problem/17825
import sys

sys.setrecursionlimit(10 ** 9)
graph = [0, 0] * 33
graph[0] = [1, 1]
graph[1] = [2, 2]
graph[2] = [3, 3]
graph[3] = [4, 4]
graph[4] = [5, 5]
graph[5] = [6, 10]
graph[6] = [7, 7]
graph[7] = [8, 8]
graph[8] = [9, 9]
graph[9] = [29, 29]
graph[10] = [11, 11]
graph[11] = [12, 12]
graph[12] = [13, 13]
graph[13] = [14, 14]
graph[14] = [15, 17]
graph[15] = [16, 16]
graph[16] = [9, 9]
graph[17] = [18, 18]
graph[18] = [19, 19]
graph[19] = [20, 20]
graph[20] = [24, 24]
graph[21] = [9, 9]
graph[22] = [21, 21]
graph[23] = [22, 22]
graph[24] = [23, 25]
graph[25] = [26, 26]
graph[26] = [27, 27]
graph[27] = [28, 28]
graph[28] = [31, 31]
graph[29] = [30, 30]
graph[30] = [31, 31]
graph[31] = [32, 32]
graph[32] = [32, 32]

score = [
    0, 2, 4, 6, 8,
    10, 13, 16, 19, 25,
    12, 14, 16, 18, 20,
    22, 24, 22, 24, 26,
    28, 26, 27, 28, 30,
    32, 34, 36, 38, 30,
    35, 40, 0
]
dice = list(map(int, input().split()))


def get_next(start, k):
    now = start
    for i in range(k):
        if i == 0:
            now = graph[now][0]
        else:
            now = graph[now][1]
    return now


def dfs(idx, s, horse):
    if idx == 10:
        global ans
        ans = max(ans, s)
        return

    for i in range(4):
        next = get_next(horse[i], dice[idx])
        flag = True
        if next != 33 - 1:
            for j in range(4):
                if i != j and next == horse[j]:
                    flag = False

        if flag:
            temp = horse[:]
            temp[i] = next
            dfs(idx + 1, s + score[next], temp)


ans = 0
dfs(0, 0, [0, 0, 0, 0])
print(ans)
