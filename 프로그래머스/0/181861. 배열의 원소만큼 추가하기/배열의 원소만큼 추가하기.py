def solution(arr):
    answer=[]
    for i in arr:
        for num in range(i):
            answer.append(i)
        
    return answer