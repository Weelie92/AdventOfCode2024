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
    matches = re.findall(r"(mul\(\d+,\d+\)|do\(\)|don't\(\))", data)

    do = True
    mul_matches = []
    
    for match in matches:
        if match == "don't()":
            print(match)
            do = False
            continue
        
        if match == "do()":
            print(match)
            do = True
            continue
            
            
        if not do:
            continue
            
        int_match = re.search(r"mul\((\d+),(\d+)\)", match)
        x, y = map(int, int_match.groups())
        mul_matches.append(x * y)
        
    total_sum = sum(mul_matches)
        

    print("Part2 sum:", total_sum)
