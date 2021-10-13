def solution(price, money, count):
    first = price
    last = price * count
    total = (first + last) * (count // 2)
    if count % 2 == 1:
        total += price * (count // 2 + 1)
    
    answer = total - money if total > money else 0
    
    return answer