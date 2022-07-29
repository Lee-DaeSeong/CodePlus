# https://www.acmicpc.net/problem/16968

string = input()

ans = 0
if string[0] == 'c':
    ans = 26
else:
    ans = 10

for i in range(1, len(string)):
    if string[i] == 'c':
        if string[i-1] == 'c':
            ans *= 25
        else:
            ans *= 26
    else:
        if string[i-1] == 'd':
            ans *= 9
        else:
            ans *= 10

print(ans)
