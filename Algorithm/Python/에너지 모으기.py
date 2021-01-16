import sys
import copy
sys.stdin = open("input.txt", "r")

def dfs(x, new_list, total):
    global max_val
    if len(new_list) <= 3:
        total += new_list[x-1] * new_list[x+1]
        max_val = max(max_val, total)
        return 0

    #print(new_list)

    result = new_list[x-1] * new_list[x+1]

    new_list.pop(x)
    length = len(new_list)
    #print("result : ", result)

    total += result
    for i in range(1, length-1):
        temp = copy.deepcopy(new_list)
        dfs(i, temp, total)

N = int(input())
energy_bolls = list(map(int, input().split()))
ans = float('-inf')
max_val = float('-inf')
for i in range(1, N-1): # 1 ~ N-2 까지
    copy_list = copy.deepcopy(energy_bolls)
    dfs(i, copy_list, 0)

print(max_val)

