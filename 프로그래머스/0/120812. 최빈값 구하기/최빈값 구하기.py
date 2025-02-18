from collections import Counter
import statistics
def solution(array):
    count = Counter(array)  
    most_common = count.most_common()  
    max_count = most_common[0][1]  
    
    modes = [key for key, value in most_common if value == max_count]
    
    return modes[0] if len(modes) == 1 else -1
    