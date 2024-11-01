def solution(n):
    answer = 0
    arr = []
    for i in str(n):
        arr.append(i)
    arr.sort()
    arr.reverse()
    print(arr)
    answer = int(''.join(arr))
        
    return answer