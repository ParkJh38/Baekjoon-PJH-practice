import math

def solution(n):
    answer = 0
    x = math.sqrt(n)
    if n == x**2 and int(x) == x:
        return (x+1)**2
    else:
        return -1
    return answer