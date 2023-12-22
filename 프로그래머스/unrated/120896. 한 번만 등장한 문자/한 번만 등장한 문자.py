from collections import Counter

def solution(s):
    result = ''
    new_S = sorted(list(s))
    cnt = Counter(new_S)
    
    answer = [element for element, count in cnt.items() if count == 1]
    for i in answer:
        result += i
    return result

