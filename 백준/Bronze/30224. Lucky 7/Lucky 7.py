N = input()

if "7" not in N and int(N) % 7 == 0:
    print(1)
elif "7" not in N and int(N) % 7 != 0:
    print(0)
elif "7" in N and int(N) % 7 == 0:
    print(3)
else:
    print(2)