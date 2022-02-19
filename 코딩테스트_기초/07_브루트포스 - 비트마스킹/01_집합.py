# https://www.acmicpc.net/problem/11723

'''
    현재 집합이 S일때

    - i를 추가      1001
    S | (1<<i)   | 0010
                 ------
                   1011

    - i를 검사      if 0 없음, else 있음
    S & (1<<i)     1011         1001
                 & 0010       & 0010
                 ------       ------
                   0010 (있음)   0000 (없음)

    - i를 제거      1011
    S & ~(1<<i)  & 1101
                 ------
                   1001

    - i를 토글     if 0 -> 1, else 1 -> 0
    S ^ (1<<i)    1001      1011
                ^ 0010    ^ 0010
                ------    ------
                  1011      1001
'''

import sys
input=sys.stdin.readline
# 전체 비트 갯수
n=20
m=int(input())
# 비트 마스킹 집합 표현
s=0

for _ in range(m):
    op, *num = sys.stdin.readline().split()
    if len(num) > 0:
        x = int(num[0])
    if op == 'add':
        s = (s | (1 << x))
    elif op == 'remove':
        s = (s & ~(1 << x))
    elif op == 'check':
        res = (s & (1 << x))
        # 해당 비트 없음
        if res == 0:
            sys.stdout.write('0\n')
        else:
            sys.stdout.write('1\n')
    elif op == 'toggle':
        s = (s ^ (1 << x))
    elif op == 'all':
        s = (1 << n)
    else:
        s = 0