https://programmers.co.kr/learn/courses/30/lessons/42747

'''
H-Index
dark
light
sublime
vim
emacs
Python3 
문제 설명
H-Index는 과학자의 생산성과 영향력을 나타내는 지표입니다. 어느 과학자의 H-Index를 나타내는 값인 h를 구하려고 합니다. 위키백과1에 따르면, H-Index는 다음과 같이 구합니다.

어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index입니다.

어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때, 이 과학자의 H-Index를 return 하도록 solution 함수를 작성해주세요.

제한사항
과학자가 발표한 논문의 수는 1편 이상 1,000편 이하입니다.
논문별 인용 횟수는 0회 이상 10,000회 이하입니다.
입출력 예
citations	return
[3, 0, 6, 1, 5]	3
입출력 예 설명
이 과학자가 발표한 논문의 수는 5편이고, 그중 3편의 논문은 3회 이상 인용되었습니다. 그리고 나머지 2편의 논문은 3회 이하 인용되었기 때문에 이 과학자의 H-Index는 3입니다.

※ 공지 - 2019년 2월 28일 테스트 케이스가 추가되었습니다.
'''

#1
def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    tmp = []
    
    for i in citations: # 전체 순환
        cnt = 0
        
        for k in citations:   # i를 포함한 나머지 배열 순환할때
            if i <= k:        # 나머지배열의 k인용횟수가 >= 해당 i번의 인용횟수보다 크거나 같으면
                cnt += 1      # i번째 인용횟수보다 인용을 했구나!!
            else : break      # 그렇지 않으면 break(sort를 했기 때문에 그 다음은 이보다 작을것임)
                
        if cnt <= i:          # h번 이상 인용된 논문이 h편 이상이고
            tmp.append(cnt)
            
    if sum(citations) == 0 : return 0   ########[0,0,0] 테케 방지     
    tmp.sort(reverse=True) #나머지 논문이 h번 이하 인용되었다면
    return tmp[0] #h의 최댓값이 이 과학자의 H-Index입니다.

#2
def solution(citations):
    citations.sort(reverse=True) #sort로 정렬해서 가장 큰값부터 작은값으로 정렬한후,
    answer = max(map(min, enumerate(citations, start=1))) #enumerate로 (index, value)형태로 묶는다. 
                               #그리고 최댓값(start = 1)부터 각 value에 대해 
                    #최솟값 value의 값을 min으로 추출하고, 그 값은 enumerate가 끝나는 citations 리스트의 크기에 해당하는 갯수가 나온다. 
                #이들을 map으로 묶으면, 한 value의 입장에서 보는 최솟값 value의 집합이 나온다. 
            #즉 h값들의 집합이나온다. h값중 최대값을 max로 뽑아서 출력하면 된다.
    return answer