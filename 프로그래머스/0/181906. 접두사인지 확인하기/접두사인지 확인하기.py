def solution(my_string, is_prefix):
    
    return 1 if my_string[:len(is_prefix)] == is_prefix else 0
    
    # a=''
    # if len(is_prefix) > len(my_string):
    #     return 0
    # for c in range(0, len(is_prefix)): 
    #     a+=my_string[c]
    # if a == is_prefix:
    #     return 1
    # else:
    #     return 0