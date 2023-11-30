from collections import Counter

S = input().upper()
count = dict(Counter(S).most_common(2))
try:
    if list(count.values())[0] == list(count.values())[1]:
        print("?")
    else:
        print(list(count.keys())[0])
except:
    print(list(count.keys())[0])