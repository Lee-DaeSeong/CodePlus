# https://www.acmicpc.net/problem/15655
import itertools

n, m = map(int, input().split())
nums=list(map(int, input().split()))
nums.sort()
for i in itertools.combinations(nums, m):
    print(*i)