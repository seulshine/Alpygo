import sys
sys.stdin = open('input.txt', 'r')

N, M, K = map(int, input().split())

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]
list_fireball = [list(map(int, input().split())) for _ in range(M)]

for i in range(0, M):
    list_fireball[i][0] = list_fireball[i][0] - 1
    list_fireball[i][1] = list_fireball[i][1] - 1

for tc in range(0, K):
    new_list_fireball = []
    fire_map = [[-1] * N for _ in range(N)]
    # 1. 모든 파이어볼이 자신의 방향 di로 속력 si칸 만큼 이동한다. 이동하는 중에는 같은 칸에 여러 개의 파이어볼이 있을 수도 있다.
    for j in range(0, len(list_fireball)):
        r, c, m, s, d = list_fireball[j]
        nr = r + (dr[d] * s)
        nc = c + (dc[d] * s)

        if nr >= N or nr < 0:
            nr = nr % N

        if nc >= N or nc < 0:
            nc = nc % N

        list_fireball[j][0] = nr
        list_fireball[j][1] = nc

        if fire_map[nr][nc] == -1:
            fire_map[nr][nc] = []
            fire_map[nr][nc].append(j)
        else:
            fire_map[nr][nc].append(j)


    # 2. 이동이 모두 끝난 뒤, 2개 이상의 파이어볼이 있는 칸에서는 다음과 같은 일이 일어난다.

    for i in range(0, N):
        for j in range(0, N):
            if fire_map[i][j] == -1:
                continue
            elif len(fire_map[i][j]) == 1:
                idx = fire_map[i][j][0]
                r, c, m , s, d = list_fireball[idx]
                new_list_fireball.append([r, c, m, s, d])
            else:
                temp = fire_map[i][j]
                sumM = 0
                sumS = 0
                two = 0
                notTwo = 0
                nr = list_fireball
                for k in range(0, len(temp)):
                    idx = temp[k]
                    if list_fireball[idx][4] % 2 == 0:
                        two = 1
                    else:
                        notTwo = 1

                    sumM = sumM + list_fireball[idx][2]
                    sumS = sumS + list_fireball[idx][3]

                newM = sumM // 5
                newS = sumS // len(temp)

                if newM == 0: # 질량이 0 이면 소멸됨
                    continue

                if two == 1 and notTwo == 1: # 모두 짝수도 홀수도 아니다.
                    new_list_fireball.append([i, j, newM, newS, 1])
                    new_list_fireball.append([i, j, newM, newS, 3])
                    new_list_fireball.append([i, j, newM, newS, 5])
                    new_list_fireball.append([i, j, newM, newS, 7])
                else:
                    new_list_fireball.append([i, j, newM, newS, 0])
                    new_list_fireball.append([i, j, newM, newS, 2])
                    new_list_fireball.append([i, j, newM, newS, 4])
                    new_list_fireball.append([i, j, newM, newS, 6])

    list_fireball = new_list_fireball

answer = 0
for i in range(0, len(list_fireball)):
    answer = answer + list_fireball[i][2]

print(answer)









