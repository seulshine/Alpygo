import sys
sys.stdin = open('input.txt', 'r')

str1 = input()
str2 = input()

len1 = len(str1)
len2 = len(str2)

len_map = [[0] * (len2 + 1) for _ in range(len1 + 1)]
answer = 0
for i in range(1, len1+1):
    for j in range(1, len2+1):
        if str1[i-1] == str2[j-1]:
            len_map[i][j] = len_map[i-1][j-1]+1
            answer = max(answer, len_map[i][j])

print(answer)