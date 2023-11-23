arr = [0]*10

for _ in range(10):
    N = int(input())
    arr[_] = (N % 42)
set1 = set(arr)
print(len(set1))