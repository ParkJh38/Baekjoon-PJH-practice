def solution(n):
    answer = []
    for each in str(n):
        answer.append(each)
    answer.reverse()
    
    int_answer = list(map(int, answer))
    
    return int_answer