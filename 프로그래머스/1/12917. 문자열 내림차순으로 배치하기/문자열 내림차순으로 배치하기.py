def solution(s):
    str = ""
    arr = list(s)
    arr.sort()
    arr.reverse()
    print(arr)
    for i in range(len(arr)):
        str += arr[i]
    return str
    



# def solution(s):
#     # sorted()를 이용해 내림차순으로 정렬 후 문자열로 합쳐서 반환
#     return ''.join(sorted(s, reverse=True))
