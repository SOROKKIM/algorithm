N = int(input())
num = 1 #벌집의 개수
cnt = 1 #벌집의 겹수

if N == 1:
    print(1)
else:
    while N > num:
        num += 6*cnt #벌집의 개수가 6의 배수만큼 증가
        cnt += 1
    print(cnt)