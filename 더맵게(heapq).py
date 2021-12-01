https://programmers.co.kr/learn/courses/30/lessons/42626

'''
더 맵게
dark
light
sublime
vim
emacs
Python3 
문제 설명
매운 것을 좋아하는 Leo는 모든 음식의 스코빌 지수를 K 이상으로 만들고 싶습니다. 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 Leo는 스코빌 지수가 가장 낮은 두 개의 음식을 아래와 같이 특별한 방법으로 섞어 새로운 음식을 만듭니다.

섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
Leo는 모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복하여 섞습니다.
Leo가 가진 음식의 스코빌 지수를 담은 배열 scoville과 원하는 스코빌 지수 K가 주어질 때, 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수를 return 하도록 solution 함수를 작성해주세요.

제한 사항
scoville의 길이는 2 이상 1,000,000 이하입니다.
K는 0 이상 1,000,000,000 이하입니다.
scoville의 원소는 각각 0 이상 1,000,000 이하입니다.
모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return 합니다.
입출력 예
scoville	K	return
[1, 2, 3, 9, 10, 12]	7	2
입출력 예 설명
스코빌 지수가 1인 음식과 2인 음식을 섞으면 음식의 스코빌 지수가 아래와 같이 됩니다.
새로운 음식의 스코빌 지수 = 1 + (2 * 2) = 5
가진 음식의 스코빌 지수 = [5, 3, 9, 10, 12]

스코빌 지수가 3인 음식과 5인 음식을 섞으면 음식의 스코빌 지수가 아래와 같이 됩니다.
새로운 음식의 스코빌 지수 = 3 + (5 * 2) = 13
가진 음식의 스코빌 지수 = [13, 9, 10, 12]

모든 음식의 스코빌 지수가 7 이상이 되었고 이때 섞은 횟수는 2회입니다.
'''

#1
import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville) #list를 minheap의 형태로
    # 전체의 반복을 이루는데 원소가 하나씩 없을때까지 하니까 최대 n-1
    while True: #모든 음식의 평균 k, 아니면 그냥 아무것도 없을때
        min1 = heapq.heappop(scoville) #최소값이 들어가
        if min1 >= K: #이미 그 min1이 K보다 크다면 안해도 되겠구나
            break
        elif len(scoville) == 0 :#제일 작은수를 뺏더니 아무것도남아ㅇ있지 않을때
            answer = -1
            break
        min2 = heapq.heappop(scoville) #두번째음식
        new_scoville = min1+2*min2 #섞어서 만든 스코빌 수준
        heapq.heappush(scoville,new_scoville)
        answer+=1

    return answer