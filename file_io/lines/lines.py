import sys

def main():
    file_name = get_file_name()
    count = get_code_lines(file_name)
    print(count)

def get_file_name():
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) >2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")
    else:
        return sys.argv[1]

def get_code_lines(file_name):
    try:
        with open(file_name) as file:
            count =0
            for line in file:
                line = line.strip()
                if line.startswith("# ") or line == "":
                    continue
                else:
                    count += 1
            return(count)
    except FileNotFoundError:
        sys.exit("File does not exist")



if __name__ == "__main__":
    main()
