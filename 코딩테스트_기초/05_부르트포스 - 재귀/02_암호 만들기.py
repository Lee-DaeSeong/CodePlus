# https://www.acmicpc.net/problem/1759

# import itertools
#
# l, c=map(int, input().split())
# char=list(input().split())
# char.sort()
# ans_list=list(map(''.join, itertools.combinations(char, l)))
#
# aeiou = ['a','e','i','o','u']
# aeiou=set(aeiou)
# ans=[]
# for string in ans_list:
#
#
#     cnt_aeiou=len(set(string)-aeiou)
#
#     if cnt_aeiou>=2 and len(string)-cnt_aeiou>=1:
#         ans.append(string)
#
# for i in sorted(ans):
#     print(i)

def check(password):
    ja = 0
    mo = 0
    for x in password:
        if x in 'aeiou':
            mo += 1
        else:
            ja += 1
    return ja >= 2 and mo >= 1

def dfs(idx, password):
    if len(password) == n:
        if check(password):
            print(password)
        return

    if idx == m:    # 종료 조건
        return

    dfs(idx+1, password+a[idx])
    dfs(idx+1, password)

n,m = map(int,input().split())
a = input().split()
a.sort()
dfs(0, '')

