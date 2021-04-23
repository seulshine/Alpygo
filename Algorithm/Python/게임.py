import sys
sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10000000)

def display(arr):
    for ii in range(len(arr)):
        for jj in range(len(arr[ii])):
            print(arr[ii][jj], end=' ')
        print()
    print()

def dfs(r, c):
    global dr, dc, visited, memo_step, board, N, M, state

    if 0 > r or r >= N or 0 > c or c >= M:
        return 0

    if board[r][c] == 'H':
        return 0

    if visited[r][c] == 1:
        state = False
        return -1

    if memo_step[r][c] != 0:
        return memo_step[r][c]

    visited[r][c] = 1

    for d in range(0, 4):
        nr = r + dr[d] * int(board[r][c])
        nc = c + dc[d] * int(board[r][c])

        memo_step[r][c] = max(memo_step[r][c], dfs(nr, nc)+1)
        if state == False:
            return -1
        # print("now : ", r, c)
        # display(memo_step)


    visited[r][c] = 0
    return memo_step[r][c]



N, M = map(int, input().split())

board = [list(input()) for _ in range(N)]
dr = [-1,0,1,0]
dc = [0,-1,0,1]
visited = [[0] * M for _ in range(N)]
memo_step = [[0] * M for _ in range(N)]
state = True
dfs(0,0)

if state == False:
    memo_step[0][0] = -1

print(memo_step[0][0])


