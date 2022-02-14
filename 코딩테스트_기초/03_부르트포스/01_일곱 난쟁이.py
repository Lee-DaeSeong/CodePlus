# https://www.acmicpc.net/source/38929320

import collections
import sys

arr=[int(input()) for _ in range(9)]

arr.sort()
total = sum(arr)
for i in range(0, 9):
    for j in range(i+1, 9):
        if total - arr[i] - arr[j] == 100:
            for k in range(0, 9):
                if not (i==k or j==k):
                    print(arr[k])
            sys.exit(0)

def dfs(idx, choice, sum_val, choice_cnt):
    if idx > 2 and choice_cnt == 0:
        return
    if sum_val > 100:
        return

    if idx == 9:
        if choice_cnt == 7 and sum_val == 100:
            print('\n'.join(map(str, sorted(choice))))
            exit()
        return

    dfs(idx + 1, choice + [arr[idx]], sum_val + arr[idx], choice_cnt + 1)
    dfs(idx + 1, choice, sum_val, choice_cnt)

def bfs():
    q=collections.deque()
    q.append([0, [], 0, 0])

    while q:

        idx, choice, sum_val, choice_cnt = q.popleft()

        if idx == 9 and choice_cnt == 7 and sum_val == 100:
            print('\n'.join(map(str, sorted(choice))))
            break

        if sum_val > 100 or choice_cnt > 7 or idx > 8:
            continue

        q.append([idx+1, choice + [arr[idx]], sum_val + arr[idx], choice_cnt+1])
        q.append([idx+1, choice, sum_val, choice_cnt])