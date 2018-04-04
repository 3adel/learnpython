from collections import deque

queue = deque(["Eric", "John", "Michael"])
print(f">>>> queue: {queue}")

queue.append("Terry")
print(f">>>> queue: {queue}")
queue.append("Graham")
print(f">>>> queue: {queue}")

popped = queue.popleft() #Eric leaves

print(f">>>> {popped} has just left")
print(f">>>> queue: {queue}")
