def solution(my_string):
    answer = my_string.translate({ord(letter): None for letter in 'aeiou'})
     
    return answer