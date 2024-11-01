def solution(s):
    if ((len(s) == 4) | (len(s)==6)):
        if s.isdecimal():
            return True
        else:
            return False
    else:
        return False