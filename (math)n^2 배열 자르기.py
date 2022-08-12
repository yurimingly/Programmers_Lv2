'''
https://school.programmers.co.kr/learn/courses/30/lessons/87390


코딩테스트 연습 - n^2 배열 자르기이미지 썸네일 삭제
코딩테스트 연습 - n^2 배열 자르기
정수 n , left , right 가 주어집니다. 다음 과정을 거쳐서 1차원 배열을 만들고자 합니다. n 행 n 열 크기의 비어있는 2차원 배열을 만듭니다. i = 1, 2, 3, ..., n 에 대해서, 다음 과정을 반복합니다. 1행 1열부터 i 행 i 열까지의 영역 내의 모든 빈 칸을 숫자 i 로 채웁니다. 1행, 2행, ..., n 행을 잘라내어 모두 이어붙인 새로운 1차원 배열을 만듭니다. 새로운 1차원 배열을 arr 이라 할 때, arr[left] , arr[left+1] , ..., arr[right] 만 남기고 나머지...

school.programmers.co.kr

n^2 배열 자르기

darklight

sublimevimemacs

문제 설명

정수 n, left, right가 주어집니다. 다음 과정을 거쳐서 1차원 배열을 만들고자 합니다.

n행 n열 크기의 비어있는 2차원 배열을 만듭니다.

i = 1, 2, 3, ..., n에 대해서, 다음 과정을 반복합니다.

1행 1열부터 i행 i열까지의 영역 내의 모든 빈 칸을 숫자 i로 채웁니다.

1행, 2행, ..., n행을 잘라내어 모두 이어붙인 새로운 1차원 배열을 만듭니다.

새로운 1차원 배열을 arr이라 할 때, arr[left], arr[left+1], ..., arr[right]만 남기고 나머지는 지웁니다.

정수 n, left, right가 매개변수로 주어집니다. 주어진 과정대로 만들어진 1차원 배열을 return 하도록 solution 함수를 완성해주세요.

제한사항

1 ≤ n ≤ 107

0 ≤ left ≤ right < n2

right - left < 105

입출력 예


0열 선택0열 다음에 열 추가
1열 선택1열 다음에 열 추가
2열 선택2열 다음에 열 추가
3열 선택3열 다음에 열 추가
0행 선택0행 다음에 행 추가
1행 선택1행 다음에 행 추가
2행 선택2행 다음에 행 추가
셀 전체 선택
열 너비 조절
행 높이 조절
n

left

right

result

3

2

5

[3,2,2,3]

4

7

14

[4,3,3,3,4,4,4,4]

셀 병합
행 분할
열 분할
너비 맞춤
삭제
입출력 예 설명

입출력 예 #1

다음 애니메이션은 주어진 과정대로 1차원 배열을 만드는 과정을 나타낸 것입니다.



사진 삭제
사진 설명을 입력하세요.

입출력 예 #2

다음 애니메이션은 주어진 과정대로 1차원 배열을 만드는 과정을 나타낸 것입니다.

'''

#성공 코드
def solution(n, left, right):
    answer = []

    for i in range(left, right + 1):
        answer.append(max(i // n, i % n) + 1)

    return answer

#효율성테스트 실패코드
def solution(n, left, right):
    tmp = [[0 for _ in range(n)] for _ in range(n)]
    print(tmp)
    
    tmp[0][0]=1
    t=0
    while(t<n):
        for i in range(t+1):
            for j in range(t+1):
                if tmp[i][j] == 0:
                    tmp[i][j] = t+1
                else:
                    continue
        t+=1
    print(tmp)
    tmp2 = []
    for i in range(n):
            for j in range(n):
                tmp2.append(tmp[i][j])
    print(tmp2)
    return tmp2[left:right+1]