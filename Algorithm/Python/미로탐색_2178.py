import sys
from collections import deque
sys.stdin = open('input.txt', 'r')

def bfs(sr,sc):
    global N, M
    que = deque()
    que.append((sr,sc,1))

    while que:
        r, c, cnt = que.popleft()

        for i in range(4):
            nr = r+dr[i]
            nc = c+dc[i]
            if 0 <= nr < N and 0 <= nc < M:
                if map[nr][nc] == 1:
                    que.append((nr, nc, cnt+1))
                    map[nr][nc] = cnt+1



N, M = map(int, input().split())

map = [list(map(int, input())) for _ in range(N)]

dr = [-1,1,0,0]
dc = [0,0,-1,1]

bfs(0,0)

print(map[N-1][M-1])