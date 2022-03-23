# https://www.acmicpc.net/problem/20327

import sys


def operation1(a):
    n = len(a)
    ans = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            ans[i][j] = a[n - i - 1][j]
    return ans


def operation5(a, l):
    n = len(a)
    ans = [[0] * n for _ in range(n)]
    sub_size = (1 << l)
    sub_count = n // sub_size
    for i in range(sub_count):
        for j in range(sub_count):
            x1 = i * sub_size
            y1 = j * sub_size
            x2 = (sub_count - i - 1) * sub_size
            y2 = j * sub_size
            for x in range(sub_size):
                for y in range(sub_size):
                    ans[x1 + x][y1 + y] = a[x2 + x][y2 + y]
    return ans


def operation2(a):
    n = len(a)
    ans = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            ans[i][j] = a[i][n - j - 1]
    return ans


def operation6(a, l):
    n = len(a)
    ans = [[0] * n for _ in range(n)]
    sub_size = (1 << l)
    sub_count = n // sub_size
    for i in range(sub_count):
        for j in range(sub_count):
            x1 = i * sub_size
            y1 = j * sub_size
            x2 = i * sub_size
            y2 = (sub_count - j - 1) * sub_size
            for x in range(sub_size):
                for y in range(sub_size):
                    ans[x1 + x][y1 + y] = a[x2 + x][y2 + y]
    return ans


def operation3(a):
    n = len(a)
    ans = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            ans[i][j] = a[n - j - 1][i]
    return ans


def operation7(a, l):
    n = len(a)
    ans = [[0] * n for _ in range(n)]
    sub_size = (1 << l)
    sub_count = n // sub_size
    for i in range(sub_count):
        for j in range(sub_count):
            x1 = i * sub_size
            y1 = j * sub_size
            x2 = (sub_count - j - 1) * sub_size
            y2 = i * sub_size
            for x in range(sub_size):
                for y in range(sub_size):
                    ans[x1 + x][y1 + y] = a[x2 + x][y2 + y]
    return ans


def operation4(a):
    n = len(a)
    ans = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            ans[i][j] = a[j][n - i - 1]
    return ans


def operation8(a, l):
    n = len(a)
    ans = [[0] * n for _ in range(n)]
    sub_size = (1 << l)
    sub_count = n // sub_size
    for i in range(sub_count):
        for j in range(sub_count):
            x1 = i * sub_size
            y1 = j * sub_size
            x2 = j * sub_size
            y2 = (sub_count - i - 1) * sub_size
            for x in range(sub_size):
                for y in range(sub_size):
                    ans[x1 + x][y1 + y] = a[x2 + x][y2 + y]
    return ans


def operation_1_to_4(a, k, sx, sy, length):
    b = [[0] * length for _ in range(length)]
    for i in range(length):
        for j in range(length):
            b[i][j] = a[sx + i][sy + j]

    if k == 1:
        b = operation1(b)
    elif k == 2:
        b = operation2(b)
    elif k == 3:
        b = operation3(b)
    elif k == 4:
        b = operation4(b)

    for i in range(length):
        for j in range(length):
            a[sx + i][sy + j] = b[i][j]


n, r = map(int, input().split())
size = (1 << n)
a = [list(map(int, input().split())) for _ in range(size)]

for _ in range(r):
    k, l = map(int, input().split())
    sub_size = (1 << l)
    if 1 <= k <= 4:
        for i in range(0, size, sub_size):
            for j in range(0, size, sub_size):
                operation_1_to_4(a, k, i, j, sub_size)
    elif 5 <= k <= 8:
        if k == 5:
            a = operation5(a, l)
        elif k == 6:
            a = operation6(a, l)
        elif k == 7:
            a = operation7(a, l)
        elif k == 8:
            a = operation8(a, l)

for i in range(size):
    print(' '.join(map(str, a[i])))
