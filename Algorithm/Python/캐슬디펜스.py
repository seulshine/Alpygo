import itertools
from collections import deque
import copy
import sys


def display(arr):
    for ii in range(len(arr)):
        for jj in range(len(arr[ii])):
            print(arr[ii][jj], end=' ')
        print()
    print()


sys.stdin = open('input.txt', 'r')
# 격자판 행의 수 N, 열의 수 M, 궁수의 공격 거리 제한 D
N, M, D = map(int, input().split())
origin_board = [list(map(int, input().split())) for _ in range(N)]

# (N+1번 행)의 모든 칸에는 성 궁수
# 궁수의 공격이 끝나면, 적이 이동한다. 적은 아래로 한 칸 이동하며, 성이 있는 칸으로 이동한 경우에는 게임에서 제외된다

arr = [0] * M
for i in range(M):
    arr[i] = i

list_comb = list(itertools.combinations(arr, 3))

num_enemy = 0
for i in range(N):
    for j in range(M):
        if origin_board[i][j] == 1:
            num_enemy += 1

answer = 0
for i in range(len(list_comb)):
    # print(list_comb[i])
    temp = 0
    visited = [[0] * M for _ in range(N)]

    board = copy.deepcopy(origin_board)
    arrow_R = N
    while 1:
        if arrow_R == 0:
            break
        if temp == num_enemy:
            break

        enemy = deque()
        for j in range(3):
            arrow = list_comb[i][j]
            len_r = 1
            distance = float('inf')
            flag = False
            for c in range(arrow - D + 1, arrow + D):
                if 0 <= c < M:
                    for r in range(1, len_r+1):
                        now_distance = r + abs(arrow - c)
                        if 0 <= arrow_R - r < arrow_R and board[arrow_R - r][c] == 1 and now_distance < distance:
                            if flag:
                                enemy.pop()

                            flag = True
                            distance = now_distance
                            enemy.append((arrow_R - r, c))

                if len_r < D and c < arrow:
                    len_r += 1
                else:
                    len_r -= 1

        # print(enemy)

        for ee in range(len(enemy)):
            r, c = enemy[ee]
            board[r][c] = 0
            if not visited[r][c]:
                temp += 1
            visited[r][c] = 1

        arrow_R -= 1

        # display(board)

    if temp > answer:
        answer = temp

print(answer)