X = int(input())
line = 1

while X > line:
    X -= line
    line += 1


if line % 2 == 0: #짝수라인 인 경우
    i = X           
    j = line - X + 1 
elif line % 2 == 1: #홀수라인 인 경우
    i = line - X + 1 
    j = X           
print(i,j, sep='/')