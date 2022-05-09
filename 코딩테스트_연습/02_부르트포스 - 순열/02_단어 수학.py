# https://www.acmicpc.net/problem/1339

import collections
import sys
import math
import itertools


n = int(input())
nums = collections.defaultdict(int)

for _ in range(n):
    string=input()

    length=len(string)
    for i, c in enumerate(string):
        nums[c] += pow(10, length-1)
        length-=1

sort_num = sorted(nums.items(), key=lambda x:x[1],  reverse=True)

ans=0
cnt=9
for i, n in sort_num:
    ans += n*cnt
    cnt-=1
print(ans)