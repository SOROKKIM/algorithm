def solution(array, n):
    answer = 0
    num = []
    cnt = 0
    for i in range(len(array)):
        array.sort()
        distance = abs(n-array[i])
        num.append(distance)
        cnt = array[num.index(min(num))]
    
    return cnt