# def solution(n, m):
#     answer = []
#     arr1 = []
#     arr2 = []
#     arr3 = []
#     for i in range(1,n+1):
#         if n % i == 0:
#             arr1.append(i)
#     for j in range(1,m+1):
#         if m % j == 0:
#             arr2.append(j)
            
#     for i in range(n):
#         for j in range(m):
#             if arr2[j] == arr1[i]:
#                 arr3.append(arr1[i])
    
#     print(arr1)
#     print(arr2)
#     print(arr3)
    
#     return answer


import math

def solution(n, m):
    g = math.gcd(n, m)  # 최대공약수 계산
    l = g * (n // g) * (m // g) # LCM  (n * m) // gcd_val  # 최소공배수 계산
    return [g, l]  # 결과 리스트 반환
