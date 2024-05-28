def solution(my_string, is_prefix):
    a=''
    if len(is_prefix) > len(my_string):
        return 0
    for c in range(0, len(is_prefix)): 
        a+=my_string[c]
    if a == is_prefix:
        return 1
    else:
        return 0