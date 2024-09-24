def solution(s):
    answer = ''
    s_list = list(s)
    s_list.sort()
    s_list.reverse()

    for i in s_list:
        answer += i
    return answer