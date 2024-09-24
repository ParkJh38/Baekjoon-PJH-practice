def solution(n):
    list = []
    list_result = []
    sum = 0
    for i in range(1, n+1):
        if (n % i) == 0:
            list.append(n // i)
        for num in list:
            if num not in list_result:
                list_result.append(num)
    list_result.sort()
    print(list_result)
    
    for j in range(len(list_result)):
        sum += list_result[j]
    
    return sum
    