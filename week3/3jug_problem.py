def get_next_states(state, caps):
    A, B, C = state
    a, b, c = caps
    states = []

    # Fill jugs
    states.append((a, B, C))
    states.append((A, b, C))
    states.append((A, B, c))

    # Empty jugs
    states.append((0, B, C))
    states.append((A, 0, C))
    states.append((A, B, 0))

    # Pour A → B
    t = min(A, b - B)
    states.append((A - t, B + t, C))

    # Pour A → C
    t = min(A, c - C)
    states.append((A - t, B, C + t))

    # Pour B → A
    t = min(B, a - A)
    states.append((A + t, B - t, C))

    # Pour B → C
    t = min(B, c - C)
    states.append((A, B - t, C + t))

    # Pour C → A
    t = min(C, a - A)
    states.append((A + t, B, C - t))

    # Pour C → B
    t = min(C, b - B)
    states.append((A, B + t, C - t))

    return states
from collections import deque

def bfs_3jug(caps, target):
    start = (0, 0, 0)
    queue = deque([(start, [start])])
    visited = set([start])

    while queue:
        state, path = queue.popleft()

        if target in state:
            return path

        for next_state in get_next_states(state, caps):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [next_state]))

    return None
def dfs_3jug(state, caps, target, visited, path):
    if target in state:
        return path

    visited.add(state)

    for next_state in get_next_states(state, caps):
        if next_state not in visited:
            result = dfs_3jug(next_state, caps, target, visited, path + [next_state])
            if result:
                return result

    return None
caps = (4, 3, 2)   # Jug capacities
target = 2        # Target amount

print("BFS Solution:")
bfs_path = bfs_3jug(caps, target)
for step in bfs_path:
    print(step)

print("\nDFS Solution:")
dfs_path = dfs_3jug((0,0,0), caps, target, set(), [(0,0,0)])
for step in dfs_path:
    print(step)

     