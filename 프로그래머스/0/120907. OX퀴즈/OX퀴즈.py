def solution(quiz):
    answer = []
    for q in quiz:
        parts = q.split(" = ")
        expression = parts[0]
        result = int(parts[1])
        
        if "+" in expression:
            nums = expression.split(" + ")
            if int(nums[0]) + int(nums[1]) == result:
                answer.append("O")
            else:
                answer.append("X")
        elif "-" in expression:
            nums = expression.split(" - ")
            if int(nums[0]) - int(nums[1]) == result:
                answer.append("O")
            else:
                answer.append("X")
    return answer