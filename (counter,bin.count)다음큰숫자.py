'''﻿https://school.programmers.co.kr/learn/courses/30/lessons/12911'''

'''
﻿
다음 큰 숫자

darklight

sublimevimemacs

문제 설명

자연수 n이 주어졌을 때, n의 다음 큰 숫자는 다음과 같이 정의 합니다.

조건 1. n의 다음 큰 숫자는 n보다 큰 자연수 입니다.

조건 2. n의 다음 큰 숫자와 n은 2진수로 변환했을 때 1의 갯수가 같습니다.

조건 3. n의 다음 큰 숫자는 조건 1, 2를 만족하는 수 중 가장 작은 수 입니다.

예를 들어서 78(1001110)의 다음 큰 숫자는 83(1010011)입니다.

자연수 n이 매개변수로 주어질 때, n의 다음 큰 숫자를 return 하는 solution 함수를 완성해주세요.

제한 사항

n은 1,000,000 이하의 자연수 입니다.

입출력 예


0열 선택0열 다음에 열 추가
1열 선택1열 다음에 열 추가
0행 선택0행 다음에 행 추가
1행 선택1행 다음에 행 추가
2행 선택2행 다음에 행 추가
셀 전체 선택
열 너비 조절
행 높이 조절
n

result

78

83

15

23

셀 병합
행 분할
열 분할
너비 맞춤
삭제
입출력 예 설명

입출력 예#1

문제 예시와 같습니다.

입출력 예#2

15(1111)의 다음 큰 숫자는 23(10111)입니다.
'''

import sys
import math
from collections import deque
from itertools import permutatio


#def1
def solution(n):
    c = bin(n).count('1')
    for m in range(n+1,1000001):
        if bin(m).count('1') == c:
            return m

# def2
from collections import Counter
def two(n):
    if n==0: return ''
    elif n % 2==0: return two(n//2)+'0'
    else: return two(n//2)+'1'

def countOne(n):
    n = two(n)
    n = Counter(list(n))
    return n['1']

def solution(n):
    cnt = countOne(n)
    for i in range(n+1,1000001):
        if cnt==(countOne(i)) : return i

