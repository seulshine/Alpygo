def solution(rows, columns, queries):
    answer = []

    dr = [0,1,0,-1] # 동남서북
    dc = [1,0,-1,0]

    num_map = [[0] * columns  for _ in range(0, rows)]
    num = 1
    for i in range(0, rows):
        for j in range(0, columns):
            num_map[i][j] = num
            num += 1

    for x1, y1, x2, y2 in queries:
        len_x = abs(x2-x1)
        len_y = abs(y2-y1)
        x1 -= 1
        y1 -= 1
        x2 -= 1
        y2 -= 1

        steps = [len_y, len_x, len_y, len_x]
        last = num_map[x1+1][y1]

        r = x1
        c = y1
        next = num_map[r][c]
        min = last

        for d in range(0, 4):
            step = steps[d]
            count = 0
            while count < step:
                r = r + dr[d]
                c = c + dc[d]

                temp = num_map[r][c]
                if temp < min:
                    min = temp

                num_map[r][c] = next
                next = temp
                count += 1

        num_map[x1][y1] = last

        answer.append(min)

    return answer



solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]])
solution(3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]])
solution(100,97,[[1,1,100,97]])