def solution(array):
    answer = 0
    array.sort()
    print(array)
    index = len(array)//2 
    answer = array[index]
    return answer