def solution(num, k):
    answer = 0
    new_num = list(str(num))
    print(new_num)
    for i in range(len(new_num)):
        if int(new_num[i]) == k:
            answer = i+1
            break
        else:
            answer = -1
    return answer