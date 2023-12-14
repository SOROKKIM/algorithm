import re
def solution(my_string):
    answer = []
    new_text = re.sub(r"[a-z]", "", my_string)
    print(new_text)
    for i in range(len(new_text)):
        answer.append(int(new_text[i]))
        answer.sort()
    return answer