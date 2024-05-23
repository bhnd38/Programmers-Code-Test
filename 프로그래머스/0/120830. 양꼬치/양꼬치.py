def solution(n, k):
    if n%10 == 0 :
        serv_count = n//10
    else:
        serv_count = n//10
    return (12000*n) + (2000*(k-serv_count))