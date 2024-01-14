def solution(a, b):
    A = int(str(a) + str(b))
    B = 2 * a * b
    if A < B :
        answer = B
    elif A > B:
        answer = A
    elif A == B:
        answer = A
    return answer