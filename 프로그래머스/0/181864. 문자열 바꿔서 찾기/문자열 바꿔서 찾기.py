def solution(myString, pat):
    myString=myString.replace('A','b')
    myString=myString.replace('B','a')
    return 1 if pat.lower() in myString else 0