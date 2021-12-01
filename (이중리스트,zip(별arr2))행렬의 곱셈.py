'''
https://programmers.co.kr/learn/courses/30/lessons/12949?language=python3

행렬의 곱셈
문제 설명
2차원 행렬 arr1과 arr2를 입력받아, arr1에 arr2를 곱한 결과를 반환하는 함수, solution을 완성해주세요.

제한 조건
행렬 arr1, arr2의 행과 열의 길이는 2 이상 100 이하입니다.
행렬 arr1, arr2의 원소는 -10 이상 20 이하인 자연수입니다.
곱할 수 있는 배열만 주어집니다.
입출력 예
arr1	arr2	return
[[1, 4], [3, 2], [4, 1]]	[[3, 3], [3, 3]]	[[15, 15], [15, 15], [15, 15]]
[[2, 3, 2], [4, 2, 4], [3, 1, 4]]	[[5, 4, 3], [2, 4, 1], [3, 1, 1]]	[[22, 22, 11], [36, 28, 18], [29, 20, 14]]
'''

def solution(arr1, arr2): #arr1 : [[1, 4], [3, 2], [4, 1]]
    answer = [[] for _ in range(len(arr1))] #[[],[],[]]
    for i in range(len(arr1)):
        tmp = [0] * len(arr2[0]) #[0,0]
        for j in range(len(arr1[0])): #열:2
            for k in range(len(arr2[0])): #행:2
                tmp[k] += arr1[i][j] * arr2[j][k] #[15,15]
        answer[i] = tmp
    return answer

#미친풀이
def solution(arr1, arr2):
    return [[sum(a*b for a, b in zip(A_row,B_col)) for B_col in zip(*arr2)] for A_row in arr1]
​