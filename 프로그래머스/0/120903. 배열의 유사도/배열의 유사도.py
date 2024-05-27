def solution(s1, s2):
    result=0
    for c in s1:
        if c in s2:
            result+=1
    return result