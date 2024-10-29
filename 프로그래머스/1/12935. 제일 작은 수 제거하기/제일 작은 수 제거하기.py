def solution(arr):
    answer = []
    if len(arr) == 1:
        return [-1]
    else:
        k = min(arr)
        for i in range(len(arr)):
            if arr[i] != k:
                answer.append(arr[i])
    return answer