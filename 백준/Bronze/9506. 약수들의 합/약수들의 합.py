answer = []
result = 0
while True:
        n = int(input())
        if n == -1:
            break
        else:
            answer = []
            result = 0
            for i in range(1, n):
                if n % i == 0:
                    answer.append(i)
            for i in answer:
                result += i
            if result == n:
                print(f'{n} = ' + " + ".join(map(str, answer)))
            else:
                print(n, "is NOT perfect.")