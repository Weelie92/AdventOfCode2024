import os


def create_day_folder(base_path: str = "."):
    base_path = os.path.abspath(base_path)

    day_folders = [d for d in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, d)) and d.startswith("Day")]
    day_number = len(day_folders) + 1
    folder_name = f"Day {day_number}"

    day_path = os.path.join(base_path, folder_name)
    os.makedirs(day_path, exist_ok=True)

    file_paths = {
        "Part1.py": os.path.join(day_path, "Part1.py"),
        "Part2.py": os.path.join(day_path, "Part2.py"),
        "Data.txt": os.path.join(day_path, "Data.txt"),
    }

    for file_name, file_path in file_paths.items():
        if not os.path.exists(file_path):  
            with open(file_path, "w") as file:
                if file_name.endswith(".py"):
                    file.write(generate_script_code(file_name.replace(".py", "")))
                elif file_name == "Data.txt":
                    file.write("")  

    print(f"Created folder and files at: {day_path}")


def generate_script_code(part_name: str) -> str:
    return f"""\
import os

def read_data(file_name="Data.txt"):
    \"\"\"Read data from a file in the current script's directory.\"\"\"
    try:
        # Get the directory of the current script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, file_name)

        # Read the file
        with open(file_path, "r") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        print(f"Error: {{file_name}} not found in {{script_dir}}.")
        return []

if __name__ == "__main__":
    data = read_data()
    print("{part_name} Data:", data)
"""


if __name__ == "__main__":
    create_day_folder()
