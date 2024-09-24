def solution(a, b):
    answer = 0
    
    if a < b:
        answer = sum(range(min(a,b), max(a,b+1))) 
    elif b < a:
        answer = sum(range(min(b,a), max(b, a+1)))
    elif a == b:
        answer = a
    return answer