def solution(a, b):
    A = int(str(a)+str(b))
    B = int(str(b)+str(a))
    if A < B :
        answer = B
    elif A > B:
        answer = A
    elif A == B:
        answer = A    
    return answer