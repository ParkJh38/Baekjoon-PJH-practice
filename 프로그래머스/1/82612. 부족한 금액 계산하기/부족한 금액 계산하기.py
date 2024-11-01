def solution(price, money, count):
    answer = -1
    total = 0
    for i in range(count):
        total += price + price * i
    if total > money:
        return total - money
    elif money >= total:
        return 0