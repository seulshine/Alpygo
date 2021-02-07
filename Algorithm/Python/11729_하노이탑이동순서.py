import sys
sys.stdin = open('input.txt', 'r')

def hanoi_move(N, start, temp, end): # 원판의 개수
    if N == 1:
        print(str(start) + " " +  str(end))
        return

    hanoi_move(N-1, start, end, temp) #가장 큰 원판을 뺀 나머지를 중간지점으로 이동
    print(str(start) + " " + str(end))
    hanoi_move(N-1, temp, start, end) #중간지점에 있던 걸 start를 중간기점으로해서 end로 옮김



N = int(input())
print(2**N - 1)
hanoi_move(N,1,2,3)
