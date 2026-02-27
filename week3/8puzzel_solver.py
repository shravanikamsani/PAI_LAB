import heapq

goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)

# Manhattan Distance heuristic
def heuristic(state):
    distance = 0
    for i in range(9):
        if state[i] != 0:
            goal_index = goal_state.index(state[i])
            distance += abs(i // 3 - goal_index // 3) + abs(i % 3 - goal_index % 3)
    return distance

# Get possible moves
def get_neighbors(state):
    neighbors = []
    index = state.index(0)
    row, col = index // 3, index % 3

    moves = [(-1,0),(1,0),(0,-1),(0,1)]

    for dr, dc in moves:
        r, c = row + dr, col + dc
        if 0 <= r < 3 and 0 <= c < 3:
            new_index = r * 3 + c
            new_state = list(state)
            new_state[index], new_state[new_index] = new_state[new_index], new_state[index]
            neighbors.append(tuple(new_state))
    return neighbors

# A* Algorithm
def solve_8_puzzle(start_state):
    open_list = []
    heapq.heappush(open_list, (heuristic(start_state), 0, start_state, []))
    visited = set()

    while open_list:
        f, g, current, path = heapq.heappop(open_list)

        if current == goal_state:
            return path + [current]

        if current in visited:
            continue
        visited.add(current)

        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                heapq.heappush(
                    open_list,
                    (g + 1 + heuristic(neighbor), g + 1, neighbor, path + [current])
                )

    return None

# Example initial state
start_state = (1, 2, 3, 4, 0, 6, 7, 5, 8)
solution = solve_8_puzzle(start_state)

# Print solution
for step in solution:
    print(step[:3])
    print(step[3:6])
    print(step[6:])
    print("-----")

                                                                                                                                 