'''
다리를 지나는 트럭
dark
light
sublime
vim
emacs
Python3 
문제 설명
트럭 여러 대가 강을 가로지르는 일차선 다리를 정해진 순으로 건너려 합니다. 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내야 합니다. 다리에는 트럭이 최대 bridge_length대 올라갈 수 있으며, 다리는 weight 이하까지의 무게를 견딜 수 있습니다. 단, 다리에 완전히 오르지 않은 트럭의 무게는 무시합니다.

예를 들어, 트럭 2대가 올라갈 수 있고 무게를 10kg까지 견디는 다리가 있습니다. 무게가 [7, 4, 5, 6]kg인 트럭이 순서대로 최단 시간 안에 다리를 건너려면 다음과 같이 건너야 합니다.

경과 시간	다리를 지난 트럭	다리를 건너는 트럭	대기 트럭
0	[]	[]	[7,4,5,6]
1~2	[]	[7]	[4,5,6]
3	[7]	[4]	[5,6]
4	[7]	[4,5]	[6]
5	[7,4]	[5]	[6]
6~7	[7,4,5]	[6]	[]
8	[7,4,5,6]	[]	[]
따라서, 모든 트럭이 다리를 지나려면 최소 8초가 걸립니다.

solution 함수의 매개변수로 다리에 올라갈 수 있는 트럭 수 bridge_length, 다리가 견딜 수 있는 무게 weight, 트럭 별 무게 truck_weights가 주어집니다. 이때 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 return 하도록 solution 함수를 완성하세요.

제한 조건
bridge_length는 1 이상 10,000 이하입니다.
weight는 1 이상 10,000 이하입니다.
truck_weights의 길이는 1 이상 10,000 이하입니다.
모든 트럭의 무게는 1 이상 weight 이하입니다.
입출력 예
bridge_length	weight	truck_weights	return
2	10	[7,4,5,6]	8
100	100	[10]	101
100	100	[10,10,10,10,10,10,10,10,10,10]	110
'''

#1 - 이게 조금더 빠른듯(sum을 쓰면 엄청 느려진다.)
from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque(0 for _ in range(bridge_length))
    total_weight = 0
    step = 0
    truck_weights.reverse()

    while truck_weights:
        total_weight -= bridge.popleft()
        if total_weight + truck_weights[-1] > weight:
            bridge.append(0)
        else:
            truck = truck_weights.pop()
            bridge.append(truck)
            total_weight += truck
        step += 1

    step += bridge_length

    return step
    
#reverse안쓰고
from collections import deque
def solution(bridge_length, weight, truck_weights):
    bridge = deque(0 for _ in range(bridge_length))
    time =0
    total = 0
    
    while truck_weights:
        total -= bridge.popleft()        
        if total + truck_weights[0] > weight:
            bridge.append(0)
        else :
            truck = truck_weights.pop(0)
            bridge.append(truck)
            total += truck
        time += 1
    time += bridge_length
    return time

#2 
bridge_length = 2
weight = 10
trucks = [7,4,5,6]

def solution(bridge_length, weight, trucks_weights): 
    time=0
    sum_bridge=0 
    bridge=[0 for _ in range(bridge_length)] 
    
    while 1: #시간의 흐름(초단위) 
        tmp=bridge.pop(0) #다리 앞부분 요소 빼냄(밑에서 조건문에 따라 0또는 트럭을 추가) 
                          #대기큐에 있는 첫번째 트럭 무게와 다리위에 있는 트럭 무게의 합이 허용범위라면 트럭을 다리위에 올림

        sum_bridge -= tmp #다리무게계산

        if len(trucks_weights)!=0 and sum_bridge+trucks_weights[0]<=weight: 
            tmp=trucks_weights.pop(0) 
            bridge.append(tmp) 
            sum_bridge+=tmp #다리무게계산 
        #아니라면 0을 다리위에
        else: 
            bridge.append(0) 
        if len(trucks_weights)==0 and sum_bridge==0: #아니라면 0을 다리위에
            break 
        time+=1
        
    return time+1

solution(bridge_length, weight, trucks_weights)