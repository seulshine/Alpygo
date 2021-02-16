import sys
sys. stdin = open('input.txt', 'r')

N = int(input())
stairs = [0] * N
for i in range(0,N):
    stairs[i] = int(input())

dp = [0] * N

for i in range(N):
    if i == 0:
        dp[0] = stairs[0]
    elif i == 1:
        dp[1] = stairs[0] + stairs[1]
    elif i == 2:
        dp[2] = max(stairs[0], stairs[1]) + stairs[2]
    else:
        dp[i] = max(dp[i-3] + stairs[i-1], dp[i-2]) + stairs[i]

print(dp[N-1])
