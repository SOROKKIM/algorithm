def solution(num, total):
    answer = []
    cnt = 0
    sum = 0
    for i in range(num):
        sum += cnt
        cnt += 1
    n = (total-sum)//num
    for i in range(num):
        answer.append(n+i)
    return answer