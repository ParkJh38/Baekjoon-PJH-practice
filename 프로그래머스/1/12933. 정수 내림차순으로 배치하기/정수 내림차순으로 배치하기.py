def solution(n):
    answer = 0
    
    first_array = []
    for each in str(n):
        first_array.append(each)
    first_array.sort()
    first_array.reverse()
    
    answer = int(''.join(first_array))
    
    return answer