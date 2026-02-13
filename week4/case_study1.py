import heapq

# A* Algorithm for Robot Path Finding

def heuristic(a, b):
    # Manhattan Distance
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(grid, start, goal):
    rows = len(grid)
    cols = len(grid[0])
    
    open_list = []
    heapq.heappush(open_list, (0, start))
    
    came_from = {}
    g_score = {start: 0}
    
    while open_list:
        _, current = heapq.heappop(open_list)
        
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path
        
        # Possible moves (Up, Down, Left, Right)
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        
        for d in directions:
            neighbor = (current[0] + d[0], current[1] + d[1])
            
            if (0 <= neighbor[0] < rows and
                0 <= neighbor[1] < cols and
                grid[neighbor[0]][neighbor[1]] == 0):
                
                tentative_g = g_score[current] + 1
                
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score = tentative_g + heuristic(neighbor, goal)
                    heapq.heappush(open_list, (f_score, neighbor))
    
    return None


# ----------- Dynamic Input Section ------------

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter grid row by row (0 = free, 1 = obstacle):")
grid = []
for i in range(rows):
    row = list(map(int, input().split()))
    grid.append(row)

start = tuple(map(int, input("Enter start position (row col): ").split()))
goal = tuple(map(int, input("Enter goal position (row col): ").split()))

path = a_star(grid, start, goal)

# ----------- Output Section ------------

if path:
    for r, c in path:
        if (r, c) != start and (r, c) != goal:
            grid[r][c] = '#'
    
    print("\nPath Matrix:")
    for row in grid:
        print(" ".join(str(cell) for cell in row))
else:
    print("No path found!")
