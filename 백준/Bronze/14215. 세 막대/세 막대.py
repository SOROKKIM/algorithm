a, b, c = map(int, input().split())

sides = [a, b, c]
sides.sort()
if sides[0] + sides[1] > sides[2]:
    print(a+b+c)
else:
    print((sides[0]+sides[1] - 1) + sides[0]+sides[1])