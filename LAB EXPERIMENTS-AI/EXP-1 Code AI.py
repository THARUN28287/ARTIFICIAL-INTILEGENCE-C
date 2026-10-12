from collections import deque

def solve(start, goal):
    queue = deque([(start, [])])
    visited = {start}

    while queue:
        state, path = queue.popleft()

        if state == goal:
            return path + [state]

        pos = state.index(0)
        row = pos // 3
        col = pos % 3

        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dr, dc in moves:
            r = row + dr
            c = col + dc

            if 0 <= r < 3 and 0 <= c < 3:
                new_pos = r * 3 + c
                new_state = list(state)

                new_state[pos], new_state[new_pos] = \
                    new_state[new_pos], new_state[pos]

                new_state = tuple(new_state)

                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, path + [state]))

    return None


start = tuple(map(int, input("Enter initial state: ").split()))
goal = tuple(map(int, input("Enter goal state: ").split()))

solution = solve(start, goal)

if solution:
    print("Solution:")
    for state in solution:
        print(state[:3])
        print(state[3:6])
        print(state[6:])
        print()
else:
    print("No solution exists")
