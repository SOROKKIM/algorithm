N = int(input())
arr = input()
values = arr.split()
values = [int(value) for value in values]
cnt = 0
answer = []

for i in values:
    cnt = 0
    for j in range(1, i+1):
        if i % j == 0:
            cnt += 1
    if cnt == 2:
        answer.append(i)
print(len(answer))