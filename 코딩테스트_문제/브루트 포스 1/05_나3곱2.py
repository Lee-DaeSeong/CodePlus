# https://www.acmicpc.net/problem/16936

n = int(input())
nums = list(map(int, input().split()))

arr = []

for num in nums:
    can3 = 0
    num_origin = num
    while True:
        if num % 3 == 0:
            can3 += 1
            num //= 3
        else:
            break
    arr.append([can3, num_origin])

arr.sort(key= lambda x: (-x[0], x[1]))
for i in range(n):
    print(arr[i][1], end=' ')