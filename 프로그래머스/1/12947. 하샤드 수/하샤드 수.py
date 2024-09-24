def solution(x):
    digit_sum = sum(int(digit) for digit in str(x))
    
    if (x % digit_sum) == 0:
        return True
    else:
        return False
    



