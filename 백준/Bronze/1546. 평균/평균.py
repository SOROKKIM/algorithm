N = int(input())
grade = list(map(int, input().split()))
grade.sort()
T = []
for i in range(N):
    T.append(grade[i] / grade[N - 1] * 100)
    
aver = sum(T) / N
print(aver)