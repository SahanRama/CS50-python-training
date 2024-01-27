months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def main():
    year, month, day = get_date()
    print(f"{year}-{month:02}-{day:02}")

def get_date():
    while True:
        try:
            date = input("Date: ").strip()
            if "/" in date:
                month, day, year = date.split("/")
                month = int(month)
                day = int(day)
                year = int(year)
                if validate_range_date(year,month,day):
                    return year,month,day
                else:
                    continue
            elif "," in date:
                month, day, year = date.split(" ")
                day = int(day.strip(","))
                year= int(year)
                month = months.index(month) +1
                if validate_range_date(year,month,day):
                    return year,month,day
                else:
                    continue
        except ValueError:
            pass

def validate_range_date(year,month,day):
    # Validate month, day, and year
    if month < 1 or month > 12:
        return False
    if day < 1 or day > 31:
        return False
    if year < 1:
        return False
    return True


if __name__ == "__main__":
    main()
