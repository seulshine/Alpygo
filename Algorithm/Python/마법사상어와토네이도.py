import sys
sys.stdin = open('input.txt', 'r')

N = int(input())

desert = [list(map(int, input().split())) for _ in range(N)]

print(desert)
# 토네이도 이동한다!
# 동 남 서 북
# 0 1 2 3
dr = [0, 1, 0, -1]
dc = [-1, 0, 1, 0]
step = 1
d = 0
count = 0
r = int(N/2)
c = int(N/2)
answer = 0
print(r, end=" ")
print(c)
# 서남동북
# 1 1 7 7 10 10 2 2 5 순서
ndr = [[-1, 1, -1, 1, -1, 1, -2, 2, 0, 0],
        [0, 0, 1, 1, 2, 2, 1, 1, 3, 2],
       [-1, 1, -1, 1, -1, 1, -2, 2, 0, 0],
       [0, 0, -1, -1, -2, -2, -1, -1, -3, -2]]

ndc = [[0, 0, -1, -1, -2, -2, -1, -1, -3, -2],
       [-1, 1, -1, 1, -1, 1, -2, 2, 0, 0],
        [0, 0, 1, 1, 2, 2, 1, 1, 3, 2],
       [-1, 1, -1, 1, -1, 1, -2, 2, 0, 0]]
percent = [0.01, 0.01, 0.07, 0.07, 0.1, 0.1, 0.02, 0.02, 0.05]

while 1:
    if r == 0 and c == 0:
        break

    next_r = 0
    next_c = 0
    if count < step:
        next_r = r + dr[d]
        next_c = c + dc[d]
        count += 1
    else:
        d = (d+1) % 4
        next_r = r + dr[d]
        next_c = c + dc[d]
        count = 1
        if d == 2 or d == 0:
            step += 1

    # print(r, end=" ")
    # print(c)

    morae = desert[next_r][next_c]
    desert[next_r][next_c] = 0
    morae_count = 0

    for i in range(0, 9):
        nr = r + ndr[d][i]
        nc = c + ndc[d][i]
        p = percent[i]

        if 0 <= nr < N and 0 <= nc < N:
            temp = int(morae * p)
            desert[nr][nc] += temp
            morae_count += temp
        else:
            temp = int(morae * p)
            answer += temp
            morae_count += temp


    r = next_r
    c = next_c

    if d == 0:
        if c-1 >= 0:
            desert[r][c-1] += morae - morae_count
        else:
            answer += morae - morae_count
    elif d == 1:
        if r+1 < N:
            desert[r+1][c] += morae - morae_count
        else:
            answer += morae - morae_count
    elif d == 2:
        if c+1 < N:
            desert[r][c+1] += morae - morae_count
        else:
            answer += morae - morae_count
    elif d == 3:
        if r-1 >= 0:
            desert[r-1][c] += morae - morae_count
        else:
            answer += morae - morae_count



print(answer)




    