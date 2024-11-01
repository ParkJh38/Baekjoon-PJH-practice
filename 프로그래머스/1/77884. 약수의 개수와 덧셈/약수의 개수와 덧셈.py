# def solution(left, right):
#     answer = 0
#     arr = []
#     k = 0
#     for num in range(left, right+1):
#         arr =[]
#         for i in range(1,num+1):
#             if (num % i) == 0:
#                 arr.append(i)
#                 k = len(arr)
#                 print(arr)
                
#                 if len(arr) % 2 == 0:
#                     answer += num
#                 else: 
#                     answer -= num
        
#     return answer

import math

def solution(left, right):
    answer = 0
    for num in range(left, right+1):
        if int(math.sqrt(num)) == math.sqrt(num):
            answer -= num
        else:
            answer += num
    return answer