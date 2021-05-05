from collections import defaultdict
import sys
sys.stdin = open('input.txt', 'r')

node = defaultdict(int)

T = int(input())

for tc in range(T):
    N = int(input())
    for i in range(N-1):
        a, b = map(int, input().split())
        node[b] = a

    nodeA, nodeB = map(int, input().split())

    parents_a = [nodeA]
    parents_b = [nodeB]

    flag_A = True
    flag_B = True
    answer = -1
    while 1:
        if flag_A:
            parentA = node[nodeA]

        # print(parentA)
        if parentA == 0:
            flag_A = False
        else:
            if flag_A:
                parents_a.append(parentA)
                nodeA = parentA

            if parentA in parents_b:
                answer = parentA
                break

        if flag_B:
            parentB = node[nodeB]

        # print(parentB)
        if parentB == 0:
            flag_B = False
        else:
            if flag_B:
                parents_b.append(parentB)
                nodeB = parentB

            if parentB in parents_a:
                answer = parentB
                break

        if flag_B == False and flag_A == False:
            break


    print(answer)
