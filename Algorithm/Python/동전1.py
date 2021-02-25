import sys
sys.stdin = open('input.txt', 'r')

# 이 동전을 적당히 사용해서, 그 가치의 합이 k원  경우의 수를
n, k = map(int, input().split())
nums = [0] * n
for i in range(0, n):
    nums[i] = int(input())

dp = [0] * (k+1)
dp[0] = 1 # 동전 자기 자신을 위한 것
for i in range(0, n):
    now = nums[i]
    for j in range(now, k+1):
        dp[j] += dp[j-now]

print(dp[k])