import heapq

goal = (1,2,3,4,5,6,7,8,0)

def heuristic(state):
    distance = 0
    for i in range(9):
        if state[i] != 0:
            goal_index = goal.index(state[i])
            distance += abs(i//3 - goal_index//3) + abs(i%3 - goal_index%3)
    return distance

def get_neighbors(state):
    neighbors = []
    index = state.index(0)
    row, col = index//3, index%3

    moves = [(-1,0),(1,0),(0,-1),(0,1)]

    for dr, dc in moves:
        r, c = row+dr, col+dc
        if 0<=r<3 and 0<=c<3:
            new_index = r*3+c
            new_state = list(state)
            new_state[index], new_state[new_index] = new_state[new_index], new_state[index]
            neighbors.append(tuple(new_state))
    return neighbors


def a_star_8_puzzle(start):
    pq = []
    heapq.heappush(pq,(heuristic(start), 0, start, []))
    visited = set()

    while pq:
        f, g, current, path = heapq.heappop(pq)

        if current == goal:
            return path + [current]

        if current in visited:
            continue
        visited.add(current)

        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                new_g = g + 1
                new_f = new_g + heuristic(neighbor)
                heapq.heappush(pq,(new_f, new_g, neighbor, path+[current]))

    return None


start_state = (1,2,3,4,0,6,7,5,8)
solution = a_star_8_puzzle(start_state)

for step in solution:
    print(step[:3])
    print(step[3:6])
    print(step[6:])
    print("------")
