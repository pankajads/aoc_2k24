def simulate_guard_path(grid):
    #print("entered")
    # Directions corresponding to 'up', 'right', 'down', and 'left'
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    direction_symbols = ['^', '>', 'v', '<']
    
    print(grid)
    # Find the initial position of the guard and determine the initial direction
    start_row, start_col = -1, -1
    initial_direction = -1
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] in direction_symbols:
                start_row, start_col = row, col
                initial_direction = direction_symbols.index(grid[row][col])
                grid[row][col] = '.'  # Remove the guard's symbol from the grid
    
    #print("debug1")
    # Initialize the guard's position and direction
    row, col = start_row, start_col
    direction = initial_direction
    #print(row, col, direction)
    visited_positions = set()  # Set to track visited positions
    print(len(grid),len(grid[row]))
    # Start simulating the guard's path
    while 0 < row < len(grid)-1 and 0 <= col < len(grid[row])-1:
        #print("while loop")
        # Mark the current position as visited
        visited_positions.add((row, col))
        
        # Check if the guard's next position is blocked
        next_row = row + directions[direction][0]
        next_col = col + directions[direction][1]
        
        #print(next_row, next_col)
        # If the next position is an obstacle, turn 90 degrees right
        if not (0 <= next_row < len(grid) and 0 <= next_col < len(grid[next_row])) or grid[next_row][next_col] == '#':
            direction = (direction + 1) % 4  # Turn right (90 degrees)
        else:
            # Move to the next position
            row, col = next_row, next_col
        #print(row, col, direction)
    
    print("debug-end")
    return len(visited_positions)

# Example input map (as given in the problem)
#Read the input file
with open("./sample_input.txt") as file:
    lines = file.readlines()

# Convert the input into a 2D array
grid = [list(line.strip()) for line in lines]

#print(grid)
# Calculate the result
result = simulate_guard_path(grid)
print(f"Number of distinct positions visited: {result}")
