import os
import re


def read_data(file_name="Data.txt"):
    """Read data from a file in the current script's directory."""
    try:
        # Get the directory of the current script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, file_name)

        # Read the file
        with open(file_path, "r") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: {file_name} not found in {script_dir}.")
        return []

if __name__ == "__main__":
    data = read_data()
    matches = re.findall(r"mul\((\d+),(\d+)\)", data)
    products = [int(x) * int(y) for x, y in matches]
    total_sum = sum(products)

    print("Part1 Data:", total_sum)
    
