arr1 = [0]*30
for i in range(30):
    arr1[i] = i+1
set1 = set(arr1)

arr2 = [0]*28
for _ in range(28):
    N = int(input())
    arr2[_] = N
set2 = set(arr2)

result = sorted(set1.difference(set2))
print(*result, sep="\n")