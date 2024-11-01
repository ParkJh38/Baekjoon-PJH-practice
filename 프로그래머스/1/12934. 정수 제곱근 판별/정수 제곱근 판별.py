import math

def solution(n):
    x = 0
    x = math.sqrt(n)
    
    if int(x) == x:
        return (x+1)**2
    else:
        return -1