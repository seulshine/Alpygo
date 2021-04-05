def solution(A):
    A.append(1)
    fib = [0] * 28
    fib[0] = 0
    fib[1] = 1
    for i in range(2, 28):
        fib[i] = fib[i-1] + fib[i-2]

    dp = [0] * (len(A))

    place = -1
    for i in range(1, 28):
        step = fib[i]
        if place+step < len(A) and A[place + step] == 1:
            dp[place+step] = 1
        if place+step >= len(A):
            break

    for i in range(0, len(A)):
        if A[i] == 1 and dp[i] >= 1:
            cnt = dp[i] + 1
            for s in range(1, 28):
                step = fib[s]
                idx = step+i
                if idx < len(A) and A[idx] == 1:
                    if dp[idx] == 0:
                        dp[idx] = cnt
                    elif dp[idx] >= 1:
                        dp[idx] = min(dp[idx], cnt)

                if idx >= len(A):
                    break

    if dp[len(A)-1] == 0:
        return -1
    else:
        return dp[len(A)-1]

solution([0,0,0,1,1,0,1,0,0,0,0])
