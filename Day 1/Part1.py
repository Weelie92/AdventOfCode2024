
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

    list1 = []
    list2 = []

    for entry in data:
        num1, num2 = map(int, entry.split())
        list1.append(num1)
        list2.append(num2)

    list1.sort()
    list2.sort()
    
    total_distance = 0

    for i in range(len(list1)):
        total_distance += abs(list1[i] - list2[i])
    
    print(f"Total distance: {total_distance}")