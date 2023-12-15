def solution(my_string):
    result = ''
    new_string = my_string.lower()
    answer = list(new_string)
    answer.sort()
    for i in range(len(answer)):
        result += answer[i]
    return result