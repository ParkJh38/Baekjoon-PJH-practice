def solution(arr):
    answer = []
    min_value = min(arr)
    arr.remove(min_value)
    if len(arr) == 0:
        return [-1]
    else:
        return arr