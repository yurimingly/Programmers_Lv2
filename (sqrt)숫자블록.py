https://school.programmers.co.kr/learn/courses/30/lessons/12923?language=python3

'''

숫자 블록

darklight

sublimevimemacs

문제 설명

그렙시에는 0으로 된 도로에 숫자 블록을 설치하기로 하였습니다. 숫자 블록의 규칙은 다음과 같습니다.

블록의 번호가 n 일 때, 가장 처음 블록은 n * 2번째 위치에 설치합니다. 그다음은 n * 3, 그다음은 n * 4, ...로 진행합니다.만약 기존에 블록이 깔려있는 자리라면 그 블록을빼고 새로운 블록으로 집어넣습니다.

예를 들어 1번 블록은 2,3,4,5, ... 인 위치에 우선 설치합니다. 그다음 2번 블록은 4,6,8,10, ... 인 위치에 설치하고, 3번 블록은 6,9,12... 인 위치에 설치합니다.

이렇게 3번 블록까지 설치하고 나면 첫 10개의 블록은 0, 1, 1, 2, 1, 3, 1, 2, 3, 2이됩니다.

그렙시는 길이가 1,000,000,000인 도로에 1번 블록부터 시작하여 10,000,000번 블록까지 위의 규칙으로 모두 놓았습니다.

그렙시의 시장님은 특정 구간의 어떤 블록이 깔려 있는지 알고 싶습니다.

구간을 나타내는 두 수 begin, end 가 매개변수로 주어 질 때, 그 구간에 깔려 있는 블록의 숫자 배열(리스트)을 return하는 solution 함수를 완성해 주세요.

제한 사항

begin, end 는 1 이상 1,000,000,000이하의 자연수 이고, begin는 항상 end보다 작습니다.

end - begin 의 값은 항상 10,000을 넘지 않습니다.

입출력 예

begin

end

result

1

10

[0, 1, 1, 2, 1, 3, 1, 4, 3, 5]

입출력 예 설명

입출력 예 #1

다음과 같이 블럭이 깔리게 됩니다.
'''

#1
import math
def solution(begin, end):
    answer = []

    for i in range(begin, end + 1):
        if i == 1:  # i == 1인 경우는 문제에서는 0으로 주어짐
            answer.append(0)
        else:
            # 소수인지 아닌지 판별하기 위해
            # 판별하기 위한 숫자 i 의 제곱근 까지 하나씩 나눠보고
            # 소수가 아니면 몫을, 소수이면 1을 넣는다.
            sqrt = int(math.sqrt(i))
            for j in range(2, sqrt + 1):
                mok = i // j
                # !!!!중요!!!! - 정확성에서는 통과하나 효율성에서 통과하지 못하는 이유가 있음
                # 전체 길이는 10**9이지만 블록은 10**7 이다
                # 그러므로 몫이 10**7을 넘어가면 안됨!!
                if mok > 10 ** 7:
                    continue
                if i % j == 0:
                    answer.append(mok)
                    break
            else:
                answer.append(1)

    return answer


#2 
def solution(begin, end):
    answer = []
    for i in range(begin, end+1):
        k = int(i != 1)  # i가 1이면 0, 1이 아니면 1을 대입
        for j in range(2, int(i**0.5)+1): # i**0.5 == sqrt(i)
            if i%j == 0 and i//j <= 10000000:
                k = i//j  # j가 2부터 커지기 때문에 처음 만나는 i//j가 약수 중 가장 큰 값
                break
        answer.append(k)
    
    return answer
