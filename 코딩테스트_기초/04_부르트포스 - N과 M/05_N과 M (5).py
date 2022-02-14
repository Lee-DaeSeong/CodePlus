# https://www.acmicpc.net/problem/15654
import itertools

n, m = map(int, input().split())
nums=list(map(int, input().split()))
nums.sort()
for i in itertools.permutations(nums, m):
    print(*i)