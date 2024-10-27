def solution(a, b):
    arr = []
    sum = 0
    t = 0
    if a <= b:
        for i in range(a,b+1):
            arr.append(i)
        for i in range(len(arr)):
            sum += arr[i]
    elif a > b:
        t = a 
        a = b
        b = t
        for i in range(a,b+1):
            arr.append(i)
        for i in range(len(arr)):
            sum += arr[i]
    return sum


