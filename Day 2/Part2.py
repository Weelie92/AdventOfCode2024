import os

def read_data(file_name="Data.txt"):
    """Read data from a file in the current script's directory."""
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, file_name)
        with open(file_path, "r") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        print(f"Error: {file_name} not found in {script_dir}.")
        return []

def is_safe(int_list):
    i = 0
    while i < len(int_list) - 1:
        current_num = int_list[i]
        next_num = int_list[i + 1]

        if i == 0:
            ascending = current_num < next_num

        if current_num == next_num:
            return False
            

        if not (0 < abs(current_num - next_num) <= 3):
            return False
            

        if ascending and current_num > next_num:
            return False
            
        elif not ascending and current_num < next_num:
            return False
        i += 1

    return True

def can_be_safe_with_removal(int_list):
    for i in range(len(int_list)):
        # Remove the current element temporarily
        removed_element = int_list.pop(i)

        if is_safe(int_list):
            int_list.insert(i, removed_element)
            return True

        # Add the removed element
        int_list.insert(i, removed_element)

    return False

if __name__ == "__main__":
    data = read_data()
    safe_reports = 0

    for report in data:
        int_list = [int(item) for item in report.split()]

        if is_safe(int_list):
            safe_reports += 1
            continue

        if can_be_safe_with_removal(int_list):
            safe_reports += 1

    print(f"Safe reports: {safe_reports}")
