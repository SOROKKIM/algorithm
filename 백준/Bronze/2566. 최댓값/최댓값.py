A = []
max_value = 0

for i in range(9):
    A.append(list(map(int, input().split())))
max_value = max(map(max, A))
print(max_value)

for i in range(9):
    for j in range(9):
        if A[i][j] == max(map(max, A)):
            print(i+1, j+1)