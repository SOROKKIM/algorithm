import math
def solution(n):
    answer = 0
    num = math.gcd(n, 6)
    answer = n//num
    return answer