def solution(phone_number):
    phone = []
    for i in phone_number:
        phone.append(i)
    print(phone)
    for i in range(0,len(phone)-4):
        phone[i] = '*' 
    print(phone)
    answer = ''.join(phone)
    print(answer)
    return answer