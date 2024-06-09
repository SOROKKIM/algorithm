import sys
input = sys.stdin.readline
from collections import deque

queue = deque()
N = int(input())

for _ in range(N):
    command = input().strip().split()
    cmd = command[0]
    
    if cmd == "push":
        queue.append(int(command[1]))
    elif cmd == "pop":
        print(queue.popleft() if queue else -1)
    elif cmd == "size":
        print(len(queue))
    elif cmd == "empty":
        print(1 if not queue else 0)
    elif cmd == "front":
        print(queue[0] if queue else -1)
    elif cmd == "back":
        print(queue[-1] if queue else -1)