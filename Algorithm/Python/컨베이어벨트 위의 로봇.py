N, K = map(int, input().split())

A = list(map(int, input().split()))

answer = 0
num_k = 0
len_A = len(A)
Robot = [0] * (N)

while 1:
    answer += 1
    # 벨트가 한 칸 회전한다.
    temp = A[len_A-1]
    A = [temp] + A[0:len_A-1]
    A = [temp] + A[0:len_A-1]

    Robot = [0] + Robot[0:N-1]
    Robot[N-1] = 0
    for i in range(N-2, -1, -1):
        if Robot[i] == 1: # 로봇이 있다!
            if A[i+1] >= 1 and Robot[i+1] == 0: # 내구도가 1이상이고 로봇이 없다.
                Robot[i+1] = 1 # 로봇 이동
                Robot[i] = 0
                A[i+1] -= 1
                if A[i+1] == 0:
                    num_k += 1
                if i+1 == N-1:
                    Robot[i+1] = 0 # 내려간다!!

    # 로봇 올린다.
    if A[0] >= 1 and Robot[0] == 0:
        A[0] -= 1
        Robot[0] = 1
        if A[0] == 0:
            num_k += 1

    if num_k >= K:
        break

print(answer)