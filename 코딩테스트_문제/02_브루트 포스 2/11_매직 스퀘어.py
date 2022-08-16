# https://www.acmicpc.net/problem/16945
import itertools
import math

maps = [list(map(int, input().split())) for _ in range(3)]


def calc():
    x = sum(temp[0])
    if x != sum(temp[1]):
        return False
    if x != sum(temp[2]):
        return False
    if x != sum([temp[0][0], temp[1][0], temp[2][0]]):
        return False
    if x != sum([temp[0][1], temp[1][1], temp[2][1]]):
        return False
    if x != sum([temp[0][2], temp[1][2], temp[2][2]]):
        return False
    if x != sum([temp[0][0], temp[1][1], temp[2][2]]):
        return False
    if x != sum([temp[0][2], temp[1][1], temp[2][0]]):
        return False
    return True

ans = math.inf
for i in itertools.permutations(range(1, 10)):
    temp = [[0] * 3 for _ in range(3)]
    idx = 0
    for j in range(3):
        for k in range(3):
            temp[j][k] = i[idx]
            idx += 1
    if calc():
        a = 0
        for j in range(3):
            for k in range(3):
                a += abs(temp[j][k] - maps[j][k])
        ans = min(a, ans)

print(ans)