# reduce와 lambda 이용하기
from functools import reduce

def solution(num_list):
    return sum(num_list) if len(num_list) >= 11 else reduce((lambda x,y:x*y), num_list)

 

# def solution(num_list):
#     answer=1
#     if len(num_list)>=11:
#         return sum(num_list)
#     else:
#         for i in num_list:
#             answer*=i
#         return answer
            
            