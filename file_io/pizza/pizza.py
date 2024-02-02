import sys
from tabulate import tabulate


def main():
    file_path = get_file_path()
    table = create_table(file_path)
    print_table(table)


def get_file_path():
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith("csv"):
        sys.exit("Not a CSV file")
    else:
        return sys.argv[1]


def create_table(file_path):
    table = []
    try:
        with open(file_path) as file:
            for line in file:
                column = line.strip().split(",")
                table.append(column)
        return table
    except FileNotFoundError:
        sys.exit("File does not exist")


def print_table(table):
    print(tabulate(table, headers="firstrow", tablefmt="grid"))


if __name__ == "__main__":
    main()
