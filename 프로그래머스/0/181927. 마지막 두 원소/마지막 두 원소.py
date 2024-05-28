def solution(num_list):
    answer = []
    n = num_list[-1] - num_list[-2]
    if n > 0:
        num_list.append(n)
    else:
        num_list.append(2*num_list[-1])
    return num_list