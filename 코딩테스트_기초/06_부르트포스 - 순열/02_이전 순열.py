# https://www.acmicpc.net/source/share/47284198034d4f81bf32053807cd100a

def prev_permutation(a):
    i = len(a)-1
    while i > 0 and a[i-1] <= a[i]:
        i -= 1
    if i <= 0:
        return False
    j = len(a)-1
    while a[j] >= a[i-1]:
        j -= 1

    a[i-1],a[j] = a[j],a[i-1]

    j = len(a)-1
    while i < j:
        a[i],a[j] = a[j],a[i]
        i += 1
        j -= 1

    return True

n = int(input())
a = list(map(int,input().split()))
if prev_permutation(a):
    print(' '.join(map(str,a)))
else:
    print(-1)
