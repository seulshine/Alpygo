N, M, K = map(int, input().split())

# 1, 2, 3, 4는 각각 위, 아래, 왼쪽, 오른쪽을 의미한다.
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

sea = [list(map(int, input().split())) for _ in range(N)]
shark_place = [0] * M
for i in range(0, N):
    for j in range(0, N):
        if sea[i][j] != 0:
            idx = sea[i][j] - 1
            shark_place[idx] = []
            shark_place[idx].append(i)
            shark_place[idx].append(j)
            sea[i][j] = []
            sea[i][j].append(idx)
            sea[i][j].append(K)

shark_dir = list(map(int, input().split()))
shark_dead = [0] * M
shark_dead_cnt = 0
dir_priority = [0] * M
for i in range(0, M):
    dir_priority[i] = []
    for j in range(0, 4):
        dir_priority[i].append(list(map(int, input().split())))

time = 1
while time < 1001:
    shark_map = [[0] * N for _ in range(N)]
    # 상어가 이동한다~~~
    for i in range(0, M):
        if shark_dead[i] == 1:
            continue

        r, c = shark_place[i]
        flag = 0
        flag2 = 0
        tr = 0
        tc = 0
        for d in range(0, 4):
            idx = dir_priority[i][shark_dir[i] - 1][d]
            nr = r + dr[idx - 1]
            nc = c + dc[idx - 1]

            if nr >= N or nr < 0 or nc >= N or nc < 0:
                continue

            if sea[nr][nc] == 0:
                flag = 1
            # elif len(sea[nr][nc]) > 1 and sea[nr][nc][1] == 1:
            #     flag = 1
            elif flag2 == 0 and len(sea[nr][nc]) > 1 and sea[nr][nc][0] == i:
                flag2 = 1
                td = d  # 방향 바꿔줌~~
                tr = nr
                tc = nc

            if flag == 1:
                # print("change dir " + str(i) + " : " + str(shark_dir[i])  + " -> " + str(dir_priority[i][shark_dir[i]-1][d]) )
                shark_dir[i] = dir_priority[i][shark_dir[i] - 1][d]  # 방향 바꿔줌~~
                shark_place[i][0] = nr
                shark_place[i][1] = nc

                if shark_map[nr][nc] == 0:
                    shark_map[nr][nc] = []
                    shark_map[nr][nc].append(i)
                else:
                    shark_map[nr][nc].append(i)
                break

        if flag == 0 and flag2 == 1:
            # print("change dir " + str(i) + " : " + str(shark_dir[i])  + " -> " + str(dir_priority[i][shark_dir[i]-1][d]) )
            shark_dir[i] = dir_priority[i][shark_dir[i] - 1][td]  # 방향 바꿔줌~~ !!! 이걸 안했었음!!!!!!!! 그래서 틀렸었음!!!
            shark_place[i][0] = tr
            shark_place[i][1] = tc

            if shark_map[tr][tc] == 0:
                shark_map[tr][tc] = []
                shark_map[tr][tc].append(i)
            else:
                shark_map[tr][tc].append(i)

    # 냄새 업데이트 and 상어 죽이기
    for i in range(0, N):
        for j in range(0, N):
            if sea[i][j] != 0:  # 냄새 업데이트
                sea[i][j][1] = sea[i][j][1] - 1
                if sea[i][j][1] == 0:
                    sea[i][j] = 0

            # 모든 상어가 이동한 후 한 칸에 여러 마리의 상어가 남아 있으면, 가장 작은 번호를 가진 상어를 제외하고 모두 격자 밖으로 쫓겨난다.
            if shark_map[i][j] == 0:  # 상어 죽이기
                continue
            else:
                sharks_len = len(shark_map[i][j])
                if sharks_len == 1:
                    sea[i][j] = []
                    sea[i][j].append(shark_map[i][j][0])
                    sea[i][j].append(K)
                else:
                    min_shark = min(shark_map[i][j])
                    for tt in range(0, sharks_len):
                        if shark_map[i][j][tt] != min_shark:
                            dead_idx = shark_map[i][j][tt]
                            shark_dead[dead_idx] = 1
                            shark_dead_cnt = shark_dead_cnt + 1  # 죽은 상어 수 + 1
                            # print("dead shark  ", end=" ")
                            # print(dead_idx)
                            # print("dead count  ", end=" ")
                            # print(shark_dead_cnt)

                    shark_map[i][j] = []
                    shark_map[i][j].append(min_shark)

                    sea[i][j] = []
                    sea[i][j].append(min_shark)
                    sea[i][j].append(K)

    if shark_dead_cnt == M - 1:
        break;

    time = time + 1
    # print("#####################" + str(time))
    # print("###########sea")
    # for i in range(0, N):
    #     for j in range(0, N):
    #         print(sea[i][j], end = " ")
    #     print()

    # print("##########shark place")
    # for i in range(0, N):
    #     for j in range(0, N):
    #         print(shark_map[i][j], end=" ")
    #     print()

if time > 1000:
    time = -1

# for i in range(0, M):
#     print(shark_place[i])
# print(shark_dir)

print(time)
