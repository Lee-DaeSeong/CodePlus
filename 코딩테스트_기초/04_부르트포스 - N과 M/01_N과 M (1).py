# https://www.acmicpc.net/problem/15649
import itertools

n, m = map(int, input().split())

# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# 순열 permutation (중복 x, 순서 o)
# for i in itertools.permutations(range(1, n+1), m):
#     print(*i)

