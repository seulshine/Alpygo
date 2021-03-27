from collections import deque
import copy
import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]
dr = [0,0,-1,1]
dc = [-1,1,0,0]
max = float('-inf')
def spread_virus():
    global max
    cnt = 0

    que = deque()
    visited = [[0] * M for _ in range(N)]
    for i in range(len(virus)):
        r, c = virus[i]
        que.append([r,c])
        visited[r][c] = 1
    while que:
        r, c = que.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < M and room[nr][nc] == 0 and not visited[nr][nc]:
                visited[nr][nc] = 1
                que.append([nr,nc])

    for i in range(N):
        for j in range(M):
            if not visited[i][j] and room[i][j] == 0:
                cnt += 1

    if max < cnt:
        max = cnt

    return

def choose_wall(r,c,depth):
    if depth == 3:
        spread_virus()
    else:
        for i in range(r, N):
            for j in range(c, M):
                if room[i][j] == 0:
                    room[i][j] = 9
                    choose_wall(i,j,depth+1)
                    room[i][j] = 0
            c = 0

virus = []

for i in range(N):
    for j in range(M):
        if room[i][j] == 2:
            virus.append([i,j])


choose_wall(0,0,0)
print(max)