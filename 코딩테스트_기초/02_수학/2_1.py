# https://www.acmicpc.net/problem/4375

while True:
    # test case가 주어지지 않는 경우 -> try, except
    try:
        n = int(input())
    except:
        break
    num = 0
    i = 1
    # N의 배수는 N을 나눈 나머지가 0
    # 1%7 = 1
    # 11%7 = (1*10+1)%7 = (1%7 * 10+1) % 7 = (1*10+1) % 7 = 4
    # 111%7 = (11*10+1)%7 = (11%7*10+1)%7 = (4*10+1)%7
    # 1111%7 = (111*10+1)%7 = (111%7*10+1)%7 = (6*10+1)%7=5
    # 11111%7 = (5*1+1)%7=2
    # 111111%7 = (2*1+1)%7=0

    while True:
        num = num * 10 + 1
        num %= n
        if num == 0:
            print(i)
            break
        i += 1
