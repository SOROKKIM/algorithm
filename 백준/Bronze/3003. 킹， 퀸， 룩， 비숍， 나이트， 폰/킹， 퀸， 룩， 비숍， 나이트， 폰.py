arr = [1, 1, 2, 2, 2, 8]
num_list = list(map(int, input().split()))
result_list = [0]*6
for i in range(len(arr)):
    result_list[i] = arr[i] - num_list[i]

for _ in range(len(result_list)):
    print(result_list[_], end=' ')