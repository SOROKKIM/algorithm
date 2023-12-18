import re

def solution(my_string):
    answer = 0
    my_string = my_string.lower()
    numbers = re.findall(r'\d+', my_string)
    answer = sum(int(number) for number in numbers)
    return answer