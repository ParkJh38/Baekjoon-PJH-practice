def solution(arr):
    answer = []
    if len(arr) == 1:
        return [-1]
    else:    
        m = min(arr)
        for i in range(len(arr)):
            if arr[i] != m:
                answer.append(arr[i])
                
    return answer