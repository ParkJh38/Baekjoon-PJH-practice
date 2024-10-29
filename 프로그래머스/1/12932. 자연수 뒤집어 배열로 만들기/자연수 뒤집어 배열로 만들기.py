def solution(n):
    answer = []
    for i in str(n):
        answer.append(i)
    answer.reverse()
    for i in range(len(answer)):
        answer[i] = int(answer[i])
    return answer


# def solution(n):  # 리스트 내포 방식
#     return [int(i) for i in str(n)[::-1]]
