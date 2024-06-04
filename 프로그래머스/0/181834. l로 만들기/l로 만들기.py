def solution(myString):
    s = ['a','b','c','d','e','f','g','h','i','j','k']
    for c in myString:
        if c in s:
            myString = myString.replace(c, 'l')
    return myString