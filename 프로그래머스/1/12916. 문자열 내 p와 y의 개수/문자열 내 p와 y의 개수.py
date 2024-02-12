def solution(s):
    answer = True
    pnum = 0
    ynum = 0
    s = s.lower()
    for i in s:
        if i == "p":
            pnum += 1
        elif i == "y":
            ynum += 1
    print(pnum)
    print(ynum)
    if pnum == ynum:
        answer = True
    else:
        answer = False
    return answer