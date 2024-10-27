def solution(s):
    if len(s) % 2 == 0: #길이 짝수
        k = len(s)//2 - 1
        #answer1 = s[k]
        #answer2 = s[k+1]
        #answer = answer1 + answer2
        answer = s[k : k+2]
    else: #길이 홀수
        answer = s[len(s)//2]
        
    return answer