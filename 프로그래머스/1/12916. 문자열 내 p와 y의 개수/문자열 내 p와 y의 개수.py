def solution(s):
    count_char = {'p': 0, 'y': 0}
    s= s.lower()
    for i in range(len(s)):
        if s[i] == 'p':
            count_char['p'] += 1
        elif s[i] == 'y':
            count_char['y'] += 1         
    if count_char['p'] == count_char['y']:
        return True
    elif count_char['p'] == 0 and count_char['y'] == 0:
        return True
    else:
        return False
    