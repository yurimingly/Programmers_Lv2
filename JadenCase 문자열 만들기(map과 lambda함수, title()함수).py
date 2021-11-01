'''
https://programmers.co.kr/learn/courses/30/lessons/12951

JadenCase 문자열 만들기
문제 설명
JadenCase란 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열입니다. 문자열 s가 주어졌을 때, s를 JadenCase로 바꾼 문자열을 리턴하는 함수, solution을 완성해주세요.

제한 조건
s는 길이 1 이상인 문자열입니다.
s는 알파벳과 공백문자(" ")로 이루어져 있습니다.
첫 문자가 영문이 아닐때에는 이어지는 영문은 소문자로 씁니다. ( 첫번째 입출력 예 참고 )
입출력 예
s	return
"3people unFollowed me"	"3people Unfollowed Me"
"for the last week"	"For The Last Week"
'''

def solution(s):
    return ' '.join(map(lambda s: s[0].upper() + s[1:].lower() if s else s, s.split(' ')))

def Jaden_Case(s):
    # 함수를 완성하세요
    answer =[]
    for i in range(len(s.split())):
        answer.append(s.split()[i][0].upper() + s.split()[i].lower()[1:]) 
    return " ".join(answer)
    
'''
def solution(s):
    answer = ''
    listt = []
    listt += s.split()
    for i in range(len(listt)):
        for k in range(len(listt[i])):
            if k==0:
                answer+=listt[i][k].upper()
            else :
                answer+=listt[i][k].lower()
        if i == len(listt)-1:
            continue
        else : answer+=" "
    return answer
'''
