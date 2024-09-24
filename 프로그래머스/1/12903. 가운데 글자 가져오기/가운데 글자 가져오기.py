def solution(s):
    length = len(s)
    if length % 2 == 1: #문자열 길이 홀수
        return s[length // 2]
    elif length % 2 == 0: #문자열 길이 짝수
        return s[length // 2 - 1 : length // 2 + 1] #슬라이싱
    return answer