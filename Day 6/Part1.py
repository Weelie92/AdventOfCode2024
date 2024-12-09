import os
import msvcrt
import time

def read_data(file_name="Data.txt"):
    """Read data from a file in the current script's directory."""
    try:
        # Get the directory of the current script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, file_name)

        # Read the file
        with open(file_path, "r") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        print(f"Error: {file_name} not found in {script_dir}.")
        return []

def rotate_right(direction):
    directions = ['^', '>', 'v', '<']
    idx = directions.index(direction)
    return directions[(idx + 1) % len(directions)]

def in_bounds(r, c, rows, cols):
    return 0 <= r < rows and 0 <= c < cols

def simulate_guard(data, grid_size=10, animate=True, delay=0.05):
    rows = len(data)
    cols = len(data[0]) if rows > 0 else 0
    grid = [list(row) for row in data]

    guard_pos = None
    guard_dir = '^'

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] in ['^', '>', 'v', '<']:
                guard_pos = (r, c)
                guard_dir = grid[r][c]
                break
        if guard_pos:
            break

    steps = 0
    cr, cc = guard_pos
    grid[cr][cc] = 'X'

    while True:
        dr, dc = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}[guard_dir]
        front_pos = (cr + dr, cc + dc)

        if not in_bounds(front_pos[0], front_pos[1], rows, cols):
            break
        elif grid[front_pos[0]][front_pos[1]] == '#':
            guard_dir = rotate_right(guard_dir)
        else:
            cr, cc = front_pos
            if grid[cr][cc] == '.':
                grid[cr][cc] = 'X'
            steps += 1

        if animate:
            draw_map(grid, (cr, cc), guard_dir, steps, grid_size)
            time.sleep(delay)
            if check_for_skip():
                print("Skipping animation...")
                animate = False

        if not animate:
            continue

    return grid, steps

def draw_map(grid, guard_pos, guard_dir, steps, grid_size):
    os.system('cls' if os.name == 'nt' else 'clear')
    rows = len(grid)
    cols = len(grid[0])
    cr, cc = guard_pos

    top = cr - grid_size // 2
    left = cc - grid_size // 2

    print(f"Steps Taken: {steps}")
    print("(Press 'S' to skip the animation)")

    for rr in range(top, top + grid_size):
        row = []
        for cc_ in range(left, left + grid_size):
            if in_bounds(rr, cc_, rows, cols):
                if (rr, cc_) == guard_pos:
                    row.append(guard_dir)
                else:
                    row.append(grid[rr][cc_])
            else:
                row.append('.')
        print("".join(row))

def check_for_skip():
    if msvcrt.kbhit():
        ch = msvcrt.getch().decode('utf-8', errors='ignore')
        if ch.lower() == 's':
            return True
    return False

def write_full_path_to_file(grid, file_name="Path1.txt"):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, file_name)
    with open(file_path, "w") as f:
        for row in grid:
            f.write("".join(row) + "\n")

if __name__ == "__main__":
    data = read_data()
    final_grid, steps_taken = simulate_guard(data, grid_size=15, animate=True, delay=0.05)

    if final_grid:
        write_full_path_to_file(final_grid, "Path1.txt")
        visited_count = sum(row.count('X') for row in final_grid)
        print("")
        print(f"Number of distinct positions visited: {visited_count}")
        print(f"Total Steps Taken: {steps_taken}")
