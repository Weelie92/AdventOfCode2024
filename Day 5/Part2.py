import os
from collections import defaultdict

def read_data(file_name="Data.txt"):
    """Read data from a file in the current script's directory."""
    try:
        # Get the directory of the current script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, file_name)

        # Read the file
        with open(file_path, "r") as file:
            lines = file.read().splitlines()

        page_order_rules = []
        pages_to_produce = []

        first_section = True

        for line in lines:
            if line.strip() == "":
                first_section = False
                continue

            if first_section:
                page_order_rules.append([int(x) for x in line.split("|")])
            else:
                pages_to_produce.append([int(x) for x in line.split(",")])

        return page_order_rules, pages_to_produce
    except FileNotFoundError:
        print(f"Error: {file_name} not found in {script_dir}.")
        return []

if __name__ == "__main__":
    page_rules, pages_to_produce = read_data()

    order = defaultdict(list)
    for rule in page_rules:
        order[rule[0]].append(rule[1])

    middle_number_sum = 0

    for page in pages_to_produce:
        invalid_page = False

        for i, num1 in enumerate(page):
            for j, num2 in enumerate(page):
                if j > i and num2 not in order[num1]:
                    to_sort = set(page)
                    new_list = []

                    for _ in range(len(to_sort)):
                        for n in list(to_sort):
                            dependencies = [n2 for n2 in to_sort if n2 != n]
                            if all(n2 not in order[n] for n2 in dependencies):
                                new_list.append(n)
                                to_sort.remove(n)
                                break

                    page = new_list
                    invalid_page = True
                    break

        if invalid_page:
            middle_number_sum += page[len(page) // 2]

    print("Part2 answer:", middle_number_sum)
