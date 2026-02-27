import heapq

# A* Water Jug Solver
def water_jug_a_star(capA, capB, target):
    start = (0, 0)
    pq = []
    heapq.heappush(pq, (0, start, []))
    visited = set()

    while pq:
        cost, (a, b), path = heapq.heappop(pq)

        if a == target or b == target:
            return path + [(a, b)]

        if (a, b) in visited:
            continue
        visited.add((a, b))

        # All possible next states
        states = [
            (capA, b),                # Fill Jug A
            (a, capB),                # Fill Jug B
            (0, b),                   # Empty Jug A
            (a, 0),                   # Empty Jug B
            (a - min(a, capB - b),    # Pour A → B
             b + min(a, capB - b)),
            (a + min(b, capA - a),    # Pour B → A
             b - min(b, capA - a))
        ]

        for state in states:
            if state not in visited:
                h = abs(state[0] - target) + abs(state[1] - target)
                heapq.heappush(
                    pq,
                    (cost + 1 + h, state, path + [(a, b)])
                )

    return None


# Example
capA = 4
capB = 3
target = 2

solution = water_jug_a_star(capA, capB, target)

# Print solution steps
for step in solution:
    print(step)
