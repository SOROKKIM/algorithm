import math
def solution(n):
    x = math.sqrt(n)
    if x.is_integer():
        result = 1
    else:
        result = 2
    return result