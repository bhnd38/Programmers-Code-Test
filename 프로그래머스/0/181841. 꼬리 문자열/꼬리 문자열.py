def solution(str_list, ex):
    
    for x in str_list:
        str_list = [x for x in str_list if ex not in x]
        # 위의 식이 좀 더 간결하다.
        
        # str_list = ['' if ex in x else x for x in str_list]
            
    return ''.join(i for i in str_list)