def solution(numbers):
    answer = 0
    answer1 = 0
    answer2 = 0
    
    numbers.sort()
    answer1 = numbers[-1]*numbers[-2]
    answer2 = numbers[0]*numbers[1]

    if answer1 > answer2:
        answer = answer1
    else:
        answer = answer2
    return answer