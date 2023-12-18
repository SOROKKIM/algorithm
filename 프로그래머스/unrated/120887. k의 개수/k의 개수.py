def solution(i, j, k):
    answer = 0
    cnt = []
    for _ in range(i, j+1):
        cnt += str(_)
    for l in range(len(cnt)):
        if str(k) == cnt[l]:
            answer += 1
    return answer