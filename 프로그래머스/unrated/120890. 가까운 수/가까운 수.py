# def solution(array, n):
#     answer = 0
#     num = []
#     cnt = 0
#     for i in range(len(array)):
#         array.sort()
#         distance = abs(n-array[i])
#         num.append(distance)
#         cnt = array[num.index(min(num))]
    
#     return cnt


def solution(array, n):
    t_list = [ ]
    array.sort()
    for i in range (len(array)):
        if n >= array[i]:
            t_list.append(n-array[i])
        elif n < array[i]:
            t_list.append(array[i]-n)
    # t_list.sort()
    x = t_list.index(min(t_list))
    return array[x]