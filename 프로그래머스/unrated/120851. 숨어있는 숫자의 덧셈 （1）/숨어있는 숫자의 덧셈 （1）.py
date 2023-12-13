def solution(my_string):
    num_list = ['1','2','3','4','5','6','7','8','9']
    answer = []
    result = 0
    for i in range(len(my_string)):
        if my_string[i] in num_list:
            answer.append(my_string[i])
    for i in range(len(answer)):
        result += int(answer[i])
    return result