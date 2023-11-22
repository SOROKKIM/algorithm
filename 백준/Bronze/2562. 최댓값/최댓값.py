arr = []

for i in range(9):
    arr.append(int(input()))

max_value = max(arr)
max_index = arr.index(max_value) + 1

print(max_value, max_index, sep="\n")