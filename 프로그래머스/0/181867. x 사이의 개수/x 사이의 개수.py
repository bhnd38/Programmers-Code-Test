def solution(myString):
    myString = myString.split('x')
    return [len(c) for c in myString]