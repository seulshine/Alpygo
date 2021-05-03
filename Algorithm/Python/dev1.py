def solution(lottos, win_nums):
    answer = []

    lowest = 0
    num_zero = 0
    for n in lottos:
        if n in win_nums:
            lowest += 1
        if n == 0:
            num_zero += 1

    highest = lowest + num_zero

    count = [6,6,5,4,3,2,1]

    answer.append(count[highest])
    answer.append(count[lowest])

    return answer



lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]

answer = solution(lottos, win_nums)
print(answer)

lottos = [0, 0, 0, 0, 0, 0]
win_nums = [38, 19, 20, 40, 15, 25]

answer = solution(lottos, win_nums)
print(answer)

lottos = [45, 4, 35, 20, 3, 9]
win_nums = [20, 9, 3, 45, 4, 35]

answer = solution(lottos, win_nums)
print(answer)