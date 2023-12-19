def solution(s):
    answer = 0
    S = s.split()
    print(S)
    prev = 0
    for i in S:
        if i == "Z":
            answer -= int(prev)
        else:
            answer += int(i)
        prev = i
    return answer