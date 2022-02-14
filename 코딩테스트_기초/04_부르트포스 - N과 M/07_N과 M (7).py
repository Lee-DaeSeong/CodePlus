# https://www.acmicpc.net/problem/15656
import itertools

n, m = map(int, input().split())
nums=list(map(int, input().split()))
nums.sort()
for i in itertools.product(nums, repeat=m):
    print(*i)