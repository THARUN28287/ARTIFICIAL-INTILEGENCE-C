
from collections import deque

def water_jug(cap1, cap2, target):
    queue = deque([(0, 0)])
    visited = {(0, 0)}

    while queue:
        a, b = queue.popleft()
        print(a, b)

        if a == target or b == target:
            print("Target reached")
            return

        states = [
            (cap1, b),
            (a, cap2),
            (0, b),
            (a, 0),
            (a - min(a, cap2 - b),
             b + min(a, cap2 - b)),
            (a + min(b, cap1 - a),
             b - min(b, cap1 - a))
        ]

        for state in states:
            if state not in visited:
                visited.add(state)
                queue.append(state)

    print("No solution exists")

cap1 = int(input("Enter Jug 1 capacity: "))
cap2 = int(input("Enter Jug 2 capacity: "))
target = int(input("Enter target amount: "))

water_jug(cap1, cap2, target)

