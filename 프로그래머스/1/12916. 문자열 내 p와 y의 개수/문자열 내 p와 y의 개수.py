# def solution(s):
#     alph_count = {'p':0, 'y':0}

#     s = ''
#     s = s.lower()
#     for i in range(len(s)):
#         if s[i] == p:
#             alph_count['p'] += 1
#         elif s[i] == y:
#             alph_count['y'] += 1
#     if alph_count['p'] == alph_count['y']:
#         print(alph_count['p'])
#         return True
#     elif alph_count['p'] != alph_count['y']:
#         return False
#     elif alph_count['p'] == 0 and alph_count['y'] == 0:
#         return True

def solution(s):
    alph_count = {'p': 0, 'y': 0}
    
    s = s.lower()
    for char in s:
        if char == 'p':
            alph_count['p'] += 1
        elif char == 'y':
            alph_count['y'] += 1

    if alph_count['p'] == alph_count['y']:
        return True
    elif alph_count['p'] != alph_count['y']:
        return False
    elif alph_count['p'] == 0 & alph_count['y'] == 0:
        return True
