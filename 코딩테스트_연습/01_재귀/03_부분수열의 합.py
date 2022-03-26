# https://www.acmicpc.net/problem/14225
import math
import sys
import collections

n = int(input())
nums = list(map(int, sys.stdin.readline().rstrip().split()))
nums.sort()
target = 1

for n in nums:
    if target < n:
        break
    target+=n
print(target)