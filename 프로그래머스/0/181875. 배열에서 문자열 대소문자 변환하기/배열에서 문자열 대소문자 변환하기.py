def solution(strArr):
    
    return [strArr[i].lower() if i%2==0 else strArr[i].upper() for i in range(len(strArr))]
    
    # for i in range(len(strArr)):
    #     if i%2==0:
    #         strArr[i]=strArr[i].lower()
    #     else:
    #         strArr[i]=strArr[i].upper()
    # return strArr