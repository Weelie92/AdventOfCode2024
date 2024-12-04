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

    total_mas = 0

    for i, line in enumerate(data):
        for j, char in enumerate(line):
            mas = 0
            if char == "A":  

                if i + 1 < len(data) and i - 1 >= 0 and j + 1 < len(line) and j - 1 >= 0:
                    # Diagonal down right
                    if data[i - 1][j - 1] ==  "M" and data[i + 1][j + 1] ==  "S":
                        mas += 1
                        
                    # Diagonal up left
                    if data[i + 1][j + 1] ==  "M" and data[i - 1][j - 1] ==  "S":
                        mas += 1

                    # Diagonal down left
                    if data[i - 1][j + 1] ==  "M" and data[i + 1][j - 1] ==  "S":
                        mas += 1

                    # Diagonal up right
                    if data[i + 1][j - 1] ==  "M" and data[i - 1][j + 1] ==  "S":
                        mas += 1
                        
                if mas == 2:
                    total_mas += 1
               

    print("Total MAS found:", total_mas)
