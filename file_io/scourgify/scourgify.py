import sys
import csv


def main():
    files = get_files()
    read_and_write_files(files)


def get_files():
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith("csv") or not sys.argv[2].endswith("csv"):
        sys.exit("Not csv files")
    else:
        return sys.argv[1], sys.argv[2]


def read_and_write_files(files):
    students = []
    try:
        with open(files[0]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                last, first = row["name"].split(", ")
                house = row["house"]
                student = {"first": first, "last": last, "house": house}
                students.append(student)
        with open(files[1], "w") as file2:
            writer = csv.DictWriter(
                file2, fieldnames=["first", "last", "house"])
            writer.writeheader()
            for student in students:
                writer.writerow(
                    {"first": student["first"], "last": student["last"], "house": student["house"]})
    except FileNotFoundError:
        sys.exit(f"Could not read {files[0]}")


if __name__ == "__main__":
    main()
