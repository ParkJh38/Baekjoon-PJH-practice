def solution(x):
    add = 0
    for i in str(x):
        add += int(i)
    if x % add == 0:
        return True
    else:
        return False