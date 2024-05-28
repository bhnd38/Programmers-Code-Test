def solution(cipher, code):
    answer=''
    n=1
    
    while n*code <= len(cipher):
        answer+=cipher[(n*code)-1]
        n+=1
        
            
    return answer