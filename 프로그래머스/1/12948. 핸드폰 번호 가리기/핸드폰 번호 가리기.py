def solution(phone_number):
    #for i in range(0, len(phone_number)-4) 
    changed_num = '*' * (len(phone_number) - 4) + phone_number[-4:]
    return changed_num

# 전화번호 문자열로 주어짐
# 전화번호 뒷 4자리를 제외한 나머지 숫자를 전부 *으로 가림 -> 가린 문자열 return 
