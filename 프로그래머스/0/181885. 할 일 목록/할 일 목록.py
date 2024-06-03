def solution(todo_list, finished):
    dict = {}
    new_dict = {}
    for i in range(len(todo_list)):
        dict[todo_list[i]] = finished[i]
        
    for k, v in dict.items():
        if v == 0:
            new_dict[k] = v
    return list(new_dict.keys())