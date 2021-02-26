import sys
sys.stdin = open('input.txt', 'r')

# 이 동전을 적당히 사용해서, 그 가치의 합이 k원  경우의 수를
n, k = map(int, input().split())
nums = [0] * n
for i in range(0, n):
    nums[i] = int(input())

dp = [100001] * (k+1)
dp[0] = 0
for i in range(0, n):
    for j in range(nums[i], k+1):
        dp[j] = min(dp[j], dp[j-nums[i]]+1)

if dp[k] == 100001:
    print(-1)
else:
    print(dp[k])