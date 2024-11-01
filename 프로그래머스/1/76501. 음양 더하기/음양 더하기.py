def solution(absolutes, signs):
    answer = 0
    for i in range(len(signs)):
        if signs[i] == True:
            absolutes[i] = absolutes[i]
        if signs[i] == False:
            absolutes[i] = 0 - absolutes[i]
        answer += int(absolutes[i])
    return answer