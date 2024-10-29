def solution(n):
    answer = 0
    str_n = str(n)
    for i in range(len(str_n)):  #인덱스 사용
        answer += int(str_n[i])
    return answer

# def solution(n):
#     answer = 0
#     for i in str(n):   #인덱스 사용하지 않고 각 자릿수 문자열로 파악
#         answer += int(i)
#     return answer