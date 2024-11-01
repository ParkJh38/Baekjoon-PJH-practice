def solution(n):
    answer = ''
    for i in range(n):
        if i % 2 == 0: #i=0,2,4 -> 수
            answer += '수'
        elif i % 2 != 0: #i=1,3,5 -> 박
            answer += '박'
    return answer