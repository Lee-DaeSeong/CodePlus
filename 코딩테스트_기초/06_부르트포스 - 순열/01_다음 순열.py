# https://www.acmicpc.net/problem/10972

def next_permutation(a):
    i = len(a)-1
    while i > 0 and a[i-1] >= a[i]: # i 찾기, a[i-1] < a[i]를 만족하는 가장 큰 i
        i -= 1
    if i <= 0:
        return False                # 내림차순 -> 마지막 순열
    j = len(a)-1
    while a[j] <= a[i-1]:           # j 찾기, a[j] > a[i-1]를 만족하는 가장 큰 j
        j -= 1

    a[i-1],a[j] = a[j],a[i-1]       # swap

    j = len(a)-1
    while i < j:                    # a[i]부터 순열 뒤집기
        a[i],a[j] = a[j],a[i]
        i += 1
        j -= 1

    return True

n = int(input())
a = list(map(int,input().split()))
if next_permutation(a):
    print(' '.join(map(str,a)))
else:
    print(-1)
