def solution(seoul):
    answer = ''
    target = 0
    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            target = i
    #return f"김서방은 {target}에 있다"
    #return ("김서방은 %d에 있다" %target)
    answer = "김서방은 "+str(target)+"에 있다"
    return answer