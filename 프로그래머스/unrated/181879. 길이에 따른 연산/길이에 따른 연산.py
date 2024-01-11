def solution(num_list):
    sumA = 1;
    lenA = len(num_list);
    if lenA >= 11:
        answer = sum(num_list);
    elif lenA <= 10:
        for i in num_list:
            sumA *= i;
        answer = sumA
    return answer