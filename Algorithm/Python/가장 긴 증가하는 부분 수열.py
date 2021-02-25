import sys
sys.stdin = open('input.txt', 'r')


N = int(input())
list_num = list(map(int, input().split()))

dp = [1] * N
for i in range(1, N):
    for j in range(0, i):
        if list_num[j] < list_num[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))

