def solution(n):
    answer = 0
    str_n = str(n)
    arr = []
    for i in str(n):
        arr.append(i)
    arr.sort()
    arr.reverse()
    answer = int(''.join(arr))
    return answer