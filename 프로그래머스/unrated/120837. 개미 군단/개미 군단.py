def solution(hp):
    cnt1 = hp // 5
    print(cnt1)
    cnt2 = (hp%5) // 3
    print(cnt2)
    cnt3 = (hp%5%3) // 1
    print(cnt3)
    answer = cnt1+cnt2+cnt3
    
    return answer