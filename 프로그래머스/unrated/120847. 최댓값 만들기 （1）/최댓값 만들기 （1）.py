def solution(numbers):
    numbers.sort()
    i = len(numbers)-1
    answer = numbers[i]*numbers[i-1]
    return answer