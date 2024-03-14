while True:
    A = int(input())
    
    if A == 0:
        break  # 입력이 0이면 반복문 종료
    
    if A % 42 == 0:
        print("PREMIADO")
    else:
        print("TENTE NOVAMENTE")
