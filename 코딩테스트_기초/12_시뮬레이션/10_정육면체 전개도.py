# https://www.acmicpc.net/problem/1917

cubes = [
    ["0010",
     "1111",
     "0010"],
    ["0100",
     "1111",
     "1000"],
    ["0010",
     "1111",
     "0100"],
    ["0001",
     "1111",
     "1000"],
    ["0001",
     "1111",
     "0100"],
    ["11100",
     "00111"],
    ["1100",
     "0111",
     "0010"],
    ["1100",
     "0111",
     "0001"],
    ["0010",
     "1110",
     "0011"],
    ["0001",
     "1111",
     "0001"],
    ["1100",
     "0110",
     "0011"]
]

def mirror(b):
    ans = []
    for i in range(len(b)):
        temp = b[i][::-1]
        ans.append(temp)
    return ans

def rotate(b):
    ans = [''] * len(b[0])
    for j in range(len(b[0])):
        for i in range(len(b)-1, -1, -1):
            ans[j] += b[i][j]
    return ans

def check(a, b, x, y):
    n = len(a)
    for i in range(len(b)):
        for j in range(len(b[0])):
                nx = x+i
                ny = y+j
                if 0 <= nx < n and 0 <= ny < n:
                    if b[i][j] == '0':
                        if a[nx][ny] == 1:
                            return False
                    elif  b[i][j] == '1':
                        if a[nx][ny] == 0:
                            return False
                else:
                    return False
    return True

t = 3
for _ in range(t):
    n = 6
    a = []
    for i in range(n):
        a.append(list(map(int,input().split())))
    ans = False
    for c in cubes:
        cube = [row[:] for row in c]
        for mir in range(2):
            for rot in range(4):
                for i in range(n):
                    for j in range(n):
                        ans |= check(a, cube, i, j)
                cube = rotate(cube)
            cube = mirror(cube)
    print("yes" if ans else "no")