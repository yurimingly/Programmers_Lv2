https://school.programmers.co.kr/learn/courses/30/lessons/12952

'''
N-Queen

문제 설명

가로, 세로 길이가 n인 정사각형으로된 체스판이 있습니다. 체스판 위의 n개의 퀸이 서로를 공격할 수 없도록 배치하고 싶습니다.

예를 들어서 n이 4인경우 다음과 같이 퀸을 배치하면 n개의 퀸은 서로를 한번에 공격 할 수 없습니다.



대표사진 삭제
사진 설명을 입력하세요.

체스판의 가로 세로의 세로의 길이 n이 매개변수로 주어질 때, n개의 퀸이 조건에 만족 하도록 배치할 수 있는 방법의 수를 return하는 solution함수를 완성해주세요.

제한사항

퀸(Queen)은 가로, 세로, 대각선으로 이동할 수 있습니다.

n은 12이하의 자연수 입니다.

입출력 예
n=4
result =2
'''


def dfs(queen, n, row):
    count = 0

    if n == row:
        return 1

    # 가로로 한번만 진행
    for col in range(n):
        queen[row] = col

        # for-else구문
        for x in range(row):
            # 세로로 겹치면 안됨
            if queen[x] == queen[row]:
                break

            # 대각선으로 겹치면 안됨
            if abs(queen[x] - queen[row]) == (row - x):
                break
        else:
            count += dfs(queen, n, row + 1)

    return count


def solution(n):
    queen = [0] * n

    return dfs(queen, n, 0)


if __name__ == "__main__":
    n = 4

    print(solution(n))