blocks = (
    ("1111"),
    ("11",
     "11"),
    ("10",
     "10",
     "11"),
    ("10",
     "11",
     "01"),
    ("111",
     "010")
)
def mirror(b):
    ans = []
    for i in range(len(b)):
        ans.append(b[i][::-1])
    return ans
def rotate(b):
    ans = ['']*len(b[0])
    for j in range(len(b[0])):
        for i in range(len(b)-1, -1, -1):
            ans[j] += b[i][j]
    return ans
def calc(a, b, x, y):
    n = len(a)
    m = len(a[0])
    s = 0
    for i in range(len(b)):
        for j in range(len(b[0])):
            if b[i][j] == '0':
                continue
            nx,ny = x+i, y+j
            if 0 <= nx < n and 0 <= ny < m:
                s += a[nx][ny]
            else:
                return -1
    return s

n,m = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(m):
        for block in blocks:
            b = block[::]
            for mir in range(2):
                for rot in range(4):
                    cur = calc(a, b, i, j)
                    if cur != -1 and ans < cur:
                        ans = cur
                    b = rotate(b)
                b = mirror(b)
print(ans)
