def solution(str_list, ex):
    
    for x in str_list:
        str_list = ['' if ex in x else x for x in str_list]
            
    return ''.join(i for i in str_list)