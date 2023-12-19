def solution(array):
    answer = 0
    num_list = []
    for i in range(len(array)):
        num_list += str(array[i])
    print(num_list)
    for l in num_list:
        if l == "7":
            answer += 1
    return answer