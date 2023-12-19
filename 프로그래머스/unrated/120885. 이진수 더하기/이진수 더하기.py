def solution(bin1, bin2):
    answer = ''
    add = int(bin1, 2) + int(bin2, 2)
    answer = bin(add)[2:]  
    return answer