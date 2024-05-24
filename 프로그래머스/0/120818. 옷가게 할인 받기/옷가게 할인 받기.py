def solution(price):
    if 100000 <= price <300000 :
        a = price*0.95
    elif 300000 <= price < 500000 :
        a = price*0.9
    elif 500000 <= price :
        a = price*0.8
    elif price < 100000 :
        a = price
    return int(a)