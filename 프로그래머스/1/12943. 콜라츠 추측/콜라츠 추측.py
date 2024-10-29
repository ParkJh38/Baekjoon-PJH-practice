def solution(num):
    answer = 0
    count = 0
    
    if num == 1:
        return 0
    
    while num != 1:
        if num % 2 == 0:
            num = num / 2
        elif num % 2 == 1:
            num = (3 * num) + 1
        count += 1
        
        if num == 1:
            return count
        if count > 500:
            return -1
    
        