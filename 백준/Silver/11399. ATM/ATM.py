N = int(input()) #사람수
A = list(map(int, input().split())) #자릿수별로 구분해 저정한 리스트
S = [0]*N #합배열

#삽입정렬

for i in range(1, N):
    insert_point = i
    insert_value = A[i]
    #j를 반복해서 현재 범위에서 삽입위치 찾기
    for j in range(i-1, -1, -1):
        if A[j] < A[i]:
            insert_point = j+1
            break
        if j == 0:
            insert_point = 0

    #삽입을 위해 데이터를 한칸 씩 뒤로 밀기
    for j in range(i, insert_point, -1):
        A[j] = A[j-1]
    A[insert_point] = insert_value #삽입 위치에 데이터 저장


S[0] = A[0]

#리스트를 통한 합배열 S 만들기
for i in range(1, N):
    S[i] = S[i-1] + A[i]

sum = 0
for i in range(0, N):
    sum += S[i]

print(sum)

