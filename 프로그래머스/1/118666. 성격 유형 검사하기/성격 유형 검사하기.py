def solution(survey, choices):
    #survey_list = ["RT", "TR", "FC", "CF", "MJ", "JM", "AN", "NA"]
    #choices_list = [1, 2, 3, 4, 5, 6, 7]
    answer = ''
    category = {"R":0, "T":0, "C":0, "F":0, "J":0, "M":0, "A":0, "N":0}
    
    for i in range(len(choices)):
        if choices[i] == 4:     #응답이 4일 경우는 점수 얻지 않음 (4->0점)
            continue
        elif choices[i] > 4:    #응답이 4보다 크면 (5->1점, 6->2점, 7->3점)
            category[survey[i][1]] += choices[i] - 4
        elif choices[i] < 4:    #응답이 4보다 작으면 (1->3점, 2->2점, 3->1점)
            category[survey[i][0]] += -choices[i] + 4
    
    if category["R"] >= category["T"]:
        answer += "R"
    else:
        answer += "T"
        
    if category["C"] >= category["F"]:
        answer += "C"
    else:
        answer += "F"
    
    if category["J"] >= category["M"]:
        answer += "J"
    else:
        answer += "M"
        
    if category["A"] >= category["N"]:
        answer += "A"
    else:
        answer += "N"
    
    return answer