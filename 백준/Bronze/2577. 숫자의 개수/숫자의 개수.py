A = int(input())
B = int(input())
C = int(input())

num = str(A*B*C)
arr = ["0","1","2","3","4","5","6","7","8","9"]
newArr = [0]*10
cnt = 0

for i in num:
    newArr[int(i)] += 1

        
for i in newArr:
    print(i)
