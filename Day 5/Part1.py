import os

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

    middle_number_sum = 0

    for page in pages_to_produce:

        valid_page = True

        for rule in page_rules:
            num1 = rule[0]
            num2 = rule[1]

            if num1 not in page or num2 not in page:
                continue  # Skip rule if irrelevant

            if page.index(num1) > page.index(num2):
                valid_page = False
                break  # Wrong order

        if valid_page:
            middle_number_sum += page[len(page) // 2]
            
    print("Part1 answer:", middle_number_sum)
