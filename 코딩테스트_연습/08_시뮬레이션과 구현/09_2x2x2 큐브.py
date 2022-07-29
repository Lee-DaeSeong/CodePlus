# https://www.acmicpc.net/problem/16939

n = 24
def check(a):
    for i in range(6):
        for j in range(4):
            if a[i*4+1] != a[i*4+j+1]:
                return False
    return True

def lu(b):
    a = b[:]
    temp = a[1]
    a[1] = a[5]
    a[5] = a[9]
    a[9] = a[24]
    a[24] = temp
    temp = a[3]
    a[3] = a[7]
    a[7] = a[11]
    a[11] = a[22]
    a[22] = temp
    return a

def ld(b):
    a = b[:]
    a = lu(a)
    a = lu(a)
    a = lu(a)
    return a

def ru(b):
    a = b[:]
    temp = a[2]
    a[2] = a[6]
    a[6] = a[10]
    a[10] = a[23]
    a[23] = temp
    temp = a[4]
    a[4] = a[8]
    a[8] = a[12]
    a[12] = a[21]
    a[21] = temp
    return a

def rd(b):
    a = b[:]
    a = ru(a)
    a = ru(a)
    a = ru(a)
    return a

def ul(b):
    a = b[:]
    temp = a[13]
    a[13] = a[5]
    a[5] = a[17]
    a[17] = a[21]
    a[21] = temp
    temp = a[14]
    a[14] = a[6]
    a[6] = a[18]
    a[18] = a[22]
    a[22] = temp
    return a

def ur(b):
    a = b[:]
    a = ul(a)
    a = ul(a)
    a = ul(a)
    return a

def dl(b):
    a = b[:]
    temp = a[15]
    a[15] = a[7]
    a[7] = a[19]
    a[19] = a[23]
    a[23] = temp
    temp = a[16]
    a[16] = a[8]
    a[8] = a[20]
    a[20] = a[24]
    a[24] = temp
    return a

def dr(b):
    a = b[:]
    a = dl(a)
    a = dl(a)
    a = dl(a)
    return a

def fl(b):
    a = b[:]
    temp = a[3]
    a[3] = a[17]
    a[17] = a[10]
    a[10] = a[16]
    a[16] = temp
    temp = a[4]
    a[4] = a[19]
    a[19] = a[9]
    a[9] = a[14]
    a[14] = temp
    return a

def fr(b):
    a = b[:]
    a = fl(a)
    a = fl(a)
    a = fl(a)
    return a

def bl(b):
    a = b[:]
    temp = a[1]
    a[1] = a[18]
    a[18] = a[12]
    a[12] = a[15]
    a[15] = temp
    temp = a[2]
    a[2] = a[20]
    a[20] = a[11]
    a[11] = a[13]
    a[13] = temp
    return a

def br(b):
    a = b[:]
    a = bl(a)
    a = bl(a)
    a = bl(a)
    return a

a = [0] + list(map(int,input().split()))
if check(lu(a)) or check(ld(a)) or check(ru(a)) or check(rd(a)):
    print(1)
elif check(ul(a)) or check(ur(a)) or check(dl(a)) or check(dr(a)):
    print(1)
elif check(fl(a)) or check(fr(a)) or check(bl(a)) or check(br(a)):
    print(1)
else:
    print(0)
