def solution(n):
    answer = []
    sum = 0
    n = str(n)
    for i in n:
        answer.append(i)
    for i in answer:
        sum += int(i)
    return sum