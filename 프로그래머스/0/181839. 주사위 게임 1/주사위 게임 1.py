def solution(a, b):
    answer = 0
    if a%2 == 1 and b%2 == 1:
        answer += a*a + b*b
    elif (a+b)%2 == 1:
        answer += 2*(a+b)
    else:
        if a<b:
            answer += -(a-b)
        else:
            answer += a-b
    return answer