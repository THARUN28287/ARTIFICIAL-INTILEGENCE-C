from collections import deque

def get_moves(state):
    moves = []
    zero = state.index(0)
    row = zero // 3
    col = zero % 3

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in directions:
        nr = row + dr
        nc = col + dc

        if 0 <= nr < 3 and 0 <= nc < 3:
            new_zero = nr * 3 + nc
            new_state = list(state)
            new_state[zero], new_state[new_zero] = new_state[new_zero], new_state[zero]
            moves.append(tuple(new_state))

    return moves


def solve(start, goal):
    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        state, path = queue.popleft()

        if state == goal:
            return path

        for new_state in get_moves(state):
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [new_state]))

    return None


def print_puzzle(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()


start = tuple(map(int, input("Enter initial state (0 for blank): ").split()))
goal = tuple(map(int, input("Enter goal state (0 for blank): ").split()))

path = solve(start, goal)

if path:
    print("\nSolution found!")
    print("Number of moves:", len(path) - 1)

    for step in path:
        print_puzzle(step)
else:
    print("No solution exists.")
