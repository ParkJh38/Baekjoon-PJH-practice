def solution(numbers):
    answer = -1
    sum = 0
    for i in numbers:
        sum += int(i)
    answer = 45 - sum
    return answer