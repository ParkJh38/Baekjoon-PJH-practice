def solution(n):
    answer = 0
    #n을 arr로 변환한 후, sort() 한 다음, 다시 int로 변환
    arr = []
    for i in str(n):
        arr.append(i)
    print(arr)
    arr.sort()
    arr.reverse()
    print(arr)
    
    #문자 리스트 arr를 하나의 문자열로 결합하고 이를 정수로 변환
    #''는 결합구분자 형태 '-' -> 1-2-3으로 결합
    answer = int(''.join(arr))
    return answer