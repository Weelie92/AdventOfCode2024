import os

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

if __name__ == "__main__":
    data = read_data()

    total_xmas = 0

    for i, line in enumerate(data):
        for j, char in enumerate(line):
            # Horizontal right
            if j + 3 < len(line):
                if char == "X" and line[j + 1] == "M" and line[j + 2] == "A" and line[j + 3] == "S":
                    total_xmas += 1

            # Horizontal left
            if j - 3 >= 0:
                if char == "X" and line[j - 1] == "M" and line[j - 2] == "A" and line[j - 3] == "S":
                    total_xmas += 1

            # Vertical down
            if i + 3 < len(data):
                if char == "X" and data[i + 1][j] == "M" and data[i + 2][j] == "A" and data[i + 3][j] == "S":
                    total_xmas += 1

            # Vertical up
            if i - 3 >= 0:
                if char == "X" and data[i - 1][j] == "M" and data[i - 2][j] == "A" and data[i - 3][j] == "S":
                    total_xmas += 1

            # Diagonal down right
            if i + 3 < len(data) and j + 3 < len(line):
                if char == "X" and data[i + 1][j + 1] == "M" and data[i + 2][j + 2] == "A" and data[i + 3][j + 3] == "S":
                    total_xmas += 1

            # Diagonal up left
            if i - 3 >= 0 and j - 3 >= 0:
                if char == "X" and data[i - 1][j - 1] == "M" and data[i - 2][j - 2] == "A" and data[i - 3][j - 3] == "S":
                    total_xmas += 1

            # Diagonal down left
            if i + 3 < len(data) and j - 3 >= 0:
                if char == "X" and data[i + 1][j - 1] == "M" and data[i + 2][j - 2] == "A" and data[i + 3][j - 3] == "S":
                    total_xmas += 1

            # Diagonal up right
            if i - 3 >= 0 and j + 3 < len(line):
                if char == "X" and data[i - 1][j + 1] == "M" and data[i - 2][j + 2] == "A" and data[i - 3][j + 3] == "S":
                    total_xmas += 1

    print(f"Total XMAS found: {total_xmas}")