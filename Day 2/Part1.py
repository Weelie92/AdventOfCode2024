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

    safe_reports = 0

    for report in data:
        split_report = report.split()
        int_list_original = [int(item) for item in split_report]

        int_list = int_list_original.copy()
        safe_report = True

        i = 0
        while i < len(int_list) - 1:
            current_num = int_list[i]
            next_num = int_list[i + 1]

            if i == 0:
                ascending = current_num < next_num

            if current_num == next_num:
                safe_report = False
                break

            if not (0 < abs(current_num - next_num) <= 3):
                safe_report = False
                break

            if ascending and current_num > next_num:
                safe_report = False
                break
            elif not ascending and current_num < next_num:
                safe_report = False
                break

            i += 1

        if safe_report:
            safe_reports += 1
            continue
    
    print(f"Safe reports: {safe_reports}")
