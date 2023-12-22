def solution(sides):
    answer = 0
    num = 0
    A = max(sides)
    B = min(sides)
    for i in range(A-B+1, A+B):
        answer += 1
        
    return answer