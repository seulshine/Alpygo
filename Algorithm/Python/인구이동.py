from collections import deque
import sys
# sys.stdin("input.txt", "r")
sys.stdin = open("input.txt", "r")


def display(arrr):
    for ii in range(len(arrr)):
        for jj in range(len(arrr[ii])):
            print(arrr[ii][jj], end=' ')
        print()
    print()

# N, L, R = map(int, input())
N, L, R = map(int, input().split())

land = [list(map(int, input().split())) for _ in range(N)]

dr = [1,-1,0,0] # 남 동만 보면 됨
dc = [0,0,-1,1]
answer = 0
while 1:
    count = 1
    union = [[0] * N for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    breakFlag = True
    for r in range(0, N):
        for c in range(0, N):
            if visited[r][c]:
                continue

            que = deque()
            que.append((r, c))
            visited[r][c] = 1
            flag = False

            while que:
                curR, curC = que.popleft()
                for d in range(4):
                    nr = curR + dr[d]
                    nc = curC + dc[d]
                    if 0 <= nr < N and 0 <= nc < N:
                        if L <= abs(land[curR][curC] - land[nr][nc]) <= R and not visited[nr][nc]:
                            visited[nr][nc] = 1
                            union[nr][nc] = count
                            union[curR][curC] = count
                            que.append((nr, nc))
                            flag = True
                            breakFlag = False

            if flag:
                count += 1

    if breakFlag:
        break

    answer += 1
    visited = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if union[r][c] > 0 and not visited[r][c]:
                arr = []
                que = deque()
                que.append((r,c))
                visited[r][c] = 1
                team = union[r][c]
                total = 0
                cnt = 0
                while que:
                    curR, curC = que.popleft()
                    total += land[curR][curC]
                    cnt += 1
                    arr.append((curR, curC))
                    for d in range(4):
                        nr = curR + dr[d]
                        nc = curC + dc[d]
                        if 0 <= nr < N and 0 <= nc < N:
                            if not visited[nr][nc] and union[nr][nc] == team:
                                visited[nr][nc] = 1
                                que.append((nr, nc))

                newValue = int(total / cnt)
                for i in range(len(arr)):
                    nowR, nowC = arr[i]
                    land[nowR][nowC] = newValue

print(answer)