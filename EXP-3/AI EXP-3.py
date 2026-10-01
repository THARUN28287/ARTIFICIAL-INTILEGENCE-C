from collections import deque

def water_jug(capacity1, capacity2, target):
    queue = deque([(0, 0)])
    visited = {(0, 0)}

    while queue:
        jug1, jug2 = queue.popleft()

        print(jug1, jug2)

        if jug1 == target or jug2 == target:
            print("Target reached")
            return

        states = [
            (capacity1, jug2),
            (jug1, capacity2),
            (0, jug2),
            (jug1, 0),
            (jug1 - min(jug1, capacity2 - jug2),
             jug2 + min(jug1, capacity2 - jug2)),
            (jug1 + min(jug2, capacity1 - jug1),
             jug2 - min(jug2, capacity1 - jug1))
        ]

        for state in states:
            if state not in visited:
                visited.add(state)
                queue.append(state)

    print("No solution exists")


capacity1 = int(input("Enter capacity of Jug 1: "))
capacity2 = int(input("Enter capacity of Jug 2: "))
target = int(input("Enter target amount: "))

water_jug(capacity1, capacity2, target)
