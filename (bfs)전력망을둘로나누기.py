'''
https://school.programmers.co.kr/learn/courses/30/lessons/86971


코딩테스트 연습 - 전력망을 둘로 나누기이미지 썸네일 삭제
코딩테스트 연습 - 전력망을 둘로 나누기
n개의 송전탑이 전선을 통해 하나의 트리 형태로 연결되어 있습니다. 당신은 이 전선들 중 하나를 끊어서 현재의 전력망 네트워크를 2개로 분할하려고 합니다. 이때, 두 전력망이 갖게 되는 송전탑의 개수를 최대한 비슷하게 맞추고자 합니다. 송전탑의 개수 n, 그리고 전선 정보 wires가 매개변수로 주어집니다. 전선들 중 하나를 끊어서 송전탑 개수가 가능한 비슷하도록 두 전력망으로 나누었을 때, 두 전력망이 가지고 있는 송전탑 개수의 차이(절대값)를 return 하도록 solution 함수를 완성해주세요. 제한사항 n은 2 이상 100...

school.programmers.co.kr

전력망을 둘로 나누기

darklight

sublimevimemacs

문제 설명

n개의 송전탑이 전선을 통해 하나의 트리 형태로 연결되어 있습니다. 당신은 이 전선들 중 하나를 끊어서 현재의 전력망 네트워크를 2개로 분할하려고 합니다. 이때, 두 전력망이 갖게 되는 송전탑의 개수를 최대한 비슷하게 맞추고자 합니다.

송전탑의 개수 n, 그리고 전선 정보 wires가 매개변수로 주어집니다. 전선들 중 하나를 끊어서 송전탑 개수가 가능한 비슷하도록 두 전력망으로 나누었을 때, 두 전력망이 가지고 있는 송전탑 개수의 차이(절대값)를 return 하도록 solution 함수를 완성해주세요.

제한사항

n은 2 이상 100 이하인 자연수입니다.

wires는 길이가 n-1인 정수형 2차원 배열입니다.

wires의 각 원소는 [v1, v2] 2개의 자연수로 이루어져 있으며, 이는 전력망의 v1번 송전탑과 v2번 송전탑이 전선으로 연결되어 있다는 것을 의미합니다.

1 ≤ v1 < v2 ≤ n 입니다.

전력망 네트워크가 하나의 트리 형태가 아닌 경우는 입력으로 주어지지 않습니다.

입출력 예


0열 선택0열 다음에 열 추가
1열 선택1열 다음에 열 추가
2열 선택2열 다음에 열 추가
0행 선택0행 다음에 행 추가
1행 선택1행 다음에 행 추가
2행 선택2행 다음에 행 추가
3행 선택3행 다음에 행 추가
셀 전체 선택
열 너비 조절
행 높이 조절
n

wires

result

9

[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]

3

4

[[1,2],[2,3],[3,4]]

0

7

[[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]

1

셀 병합
행 분할
열 분할
너비 맞춤
삭제
입출력 예 설명

입출력 예 #1

다음 그림은 주어진 입력을 해결하는 방법 중 하나를 나타낸 것입니다.



사진 삭제
사진 설명을 입력하세요.

4번과 7번을 연결하는 전선을 끊으면 두 전력망은 각 6개와 3개의 송전탑을 가지며, 이보다 더 비슷한 개수로 전력망을 나눌 수 없습니다.

또 다른 방법으로는 3번과 4번을 연결하는 전선을 끊어도 최선의 정답을 도출할 수 있습니다.

입출력 예 #2

다음 그림은 주어진 입력을 해결하는 방법을 나타낸 것입니다.



사진 삭제
사진 설명을 입력하세요.

2번과 3번을 연결하는 전선을 끊으면 두 전력망이 모두 2개의 송전탑을 가지게 되며, 이 방법이 최선입니다.

입출력 예 #3

다음 그림은 주어진 입력을 해결하는 방법을 나타낸 것입니다.



사진 삭제
사진 설명을 입력하세요.

3번과 7번을 연결하는 전선을 끊으면 두 전력망이 각각 4개와 3개의 송전탑을 가지게 되며, 이 방법이 최선입니다.

﻿'''

#def1
from collections import defaultdict, deque


def bfs_and_node_count(del_line, n, wire_dict):
    count = 1  # 연결된 노드의 수
    visited = [False] * (n + 1)  # 방문여부 체크
    visited[del_line[0]] = True  # 시작노드방문처리
    queue = deque([del_line[0]])

    while queue:  # bfs수행
        curr = queue.popleft()
        for i in wire_dict[curr]:  # curr노드와 연결된 노드에 대해서
            if visited[i] or i == del_line[1]:  # 방문했거나 끊어지는 부분의 노드인 경우는 패스
                continue
            count += 1
            queue.append(i)
            visited[i] = True
    return count


def solution(n, wires):
    answer = 1000
    data = defaultdict(set)  # 각 노드와 연결된 노드 정보
    for a, b in wires:
        data[a].add(b)
        data[b].add(a)
        print(a, b)
    for w in wires:
        # 해당 와이어를 끊었을 때 한 쪽 영역의 노드 수 구하기
        temp = bfs_and_node_count(w, n, data)

        # 기존 answer와 현재 해당하는 와이어를 끊었을 때 노드 차이 비교해서 최솟값으로 업데이트
        answer = min(answer, abs(n - temp - temp))
    return answer

#def2
import sys
import math
import re
from collections import deque
from collections import Counter
from itertools import permutations
from itertools import product
sys.stdin=open("input.txt","r")


def solution(n, wires):
    ans = n
    for sub in (wires[i+1:] + wires[:i] for i in range(len(wires))):
        s = set(sub[0])
        [s.update(v) for _ in sub for v in sub if set(v) & s]
        ans = min(ans, abs(2 * len(s) - n))
    return ans

if __name__=="__main__":

    n = 9
    wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
    solution(n,wires)
