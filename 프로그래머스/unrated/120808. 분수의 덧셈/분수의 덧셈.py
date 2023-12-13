import math

def solution(numer1, denom1, numer2, denom2):
    answer = []
    numer = int(numer1*denom2+numer2*denom1)
    denom = int(denom1*denom2)
    i = math.gcd(numer, denom)
    answer.append(numer//i)
    answer.append(denom//i)
    
    return answer