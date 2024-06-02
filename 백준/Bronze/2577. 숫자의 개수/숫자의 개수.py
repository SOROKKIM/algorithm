A = int(input())
B = int(input())
C = int(input())

num = str(A*B*C)
newArr = [0]*10
for i in num:
    newArr[int(i)] += 1

        
for i in newArr:
    print(i)
