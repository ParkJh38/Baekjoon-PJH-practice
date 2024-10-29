def solution(arr):
    average = 0
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
        average = sum / len(arr)
    return average