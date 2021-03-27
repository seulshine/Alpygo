import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]


dr, dc = (-1, 0, 1, 0), (0, 1, 0, -1) # 북, 동, 남, 서

answer = 0

while 1:
    if room[r][c] == 0:
        room[r][c] = 7
        answer += 1

    move = False
    for i in range(0, 4):
        d = (d+3) % 4
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < N and 0 <= nc < M and room[nr][nc] == 0:
            r = nr
            c = nc
            move = True
            break

    if not move:
        nr = r - dr[d]
        nc = c - dc[d]
        if 0 <= nr < N and 0 <= nc < M and room[nr][nc] == 1:
            break
        else:
            r = nr
            c = nc

print(answer)