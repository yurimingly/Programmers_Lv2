https://school.programmers.co.kr/learn/courses/30/lessons/12946

'''
하노이의 탑

darklight

sublimevimemacs

문제 설명

하노이 탑(Tower of Hanoi)은 퍼즐의 일종입니다. 세 개의 기둥과 이 기동에 꽂을 수 있는 크기가 다양한 원판들이 있고, 퍼즐을 시작하기 전에는 한 기둥에 원판들이 작은 것이 위에 있도록 순서대로 쌓여 있습니다. 게임의 목적은 다음 두 가지 조건을 만족시키면서, 한 기둥에 꽂힌 원판들을 그 순서 그대로 다른 기둥으로 옮겨서 다시 쌓는 것입니다.

한 번에 하나의 원판만 옮길 수 있습니다.

큰 원판이 작은 원판 위에 있어서는 안됩니다.

하노이 탑의 세 개의 기둥을 왼쪽 부터 1번, 2번, 3번이라고 하겠습니다. 1번에는 n개의 원판이 있고 이 n개의 원판을 3번 원판으로 최소 횟수로 옮기려고 합니다.

1번 기둥에 있는 원판의 개수 n이 매개변수로 주어질 때, n개의 원판을 3번 원판으로 최소로 옮기는 방법을 return하는 solution를 완성해주세요.

제한사항

n은 15이하의 자연수 입니다.

입출력 예


0열 선택0열 다음에 열 추가
1열 선택1열 다음에 열 추가
0행 선택0행 다음에 행 추가
1행 선택1행 다음에 행 추가
셀 전체 선택
열 너비 조절
행 높이 조절
n

result

2

[ [1,2], [1,3], [2,3] ]

셀 병합
행 분할
열 분할
너비 맞춤
삭제
입출력 예 설명

입출력 예 #1

다음과 같이 옮길 수 있습니다.
'''

hanoi = []


def han(n, first, semi, final):  # 원판의 개수, 처음시작하는 기둥, 중간기둥
    # 마지막 기둥을 매개변수로 받는 함수
    #####start,mid,end같은 느낌으로 함수를 바라봐야한다.#####
    if n == 1:  # 원판이 하나 일 때는
        hanoi.append([first, final])  # 배열에 첫번째에서 세번째로 옮긴다는 라는 뜻으로
        # [first,final] 을 추가해준다.
    else:  # 원판이 하나가 아닐 때는 아래와 같은 과정을 수행한다.
        han(n - 1, first, final, semi)  # n-1개의 원판을 첫번째에서 중간으로 옮기고
        ###첫번째에서 중간으로 옮긴다. 위치가 start,mid,end인데 first=start , end위치에 mid(=semi)가 들어간거
        han(1, first, semi, final)  # 1개의 원판을 첫번째에서 마지막으로
        han(n - 1, semi, first, final)  # 다시 n-1개의 원판을 중간에서 마지막으로 옮긴다.

    return hanoi  # hanoi 배열을 결과 값으로 return 하고


def solution(n):  # 문제를 해결하는 함수
    answer = han(n, 1, 2, 3)  # 첫번째 기둥에서 두 번째 기둥을 통해 세번째 기둥으로 n개의 원판을 옮긴다.
    return answer

if __name__ == "__main__":
    n = 4

    print(solution(n))