import sys
sys.stdin = open('input.txt', 'r')

def moo_game(N, idx):
    global ans
    if idx == 0:
        if N == 1:
            ans = "m"
        else:
            ans = "o"
        return

    if list_length[idx - 1] < N <= list_length[idx - 1] + idx + 3:  # 가운데 끼여있다면
        if N == list_length[idx - 1] + 1:
            ans = "m"
        else:
            ans = "o"
    elif N < list_length[idx-1]:
        moo_game(N, idx-1)
    else:
        moo_game(N-(idx+3+list_length[idx-1]), idx-1)


# S(k)는 S(k-1)과 o가 k+2개인 수열 "m o ... o" 와 S(k-1)
# S(k) = S(k-1) + k + 3 (= m + o(k+2)) + S(k-1)
N = int(input())
idx = -1
list_length = [3]
for i in range(1, 28):
    list_length.append(2 * list_length[i-1] + i + 3)
    if idx == -1 and N < list_length[i]:
        idx = i

ans = ""
moo_game(N, idx)

print(ans)