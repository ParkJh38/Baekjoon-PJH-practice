def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer += int(a[i]*b[i])
    return answer