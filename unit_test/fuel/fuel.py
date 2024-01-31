def main():
    while True:
        fraction = input("Fraction: ")
        try:
            percentage = convert(fraction)
            if percentage >=0:
                fuel_gauge = gauge(percentage)
                print(fuel_gauge)
                break
        except (ValueError, ZeroDivisionError):
            pass


def convert(fraction):
    x, y = fraction.split("/")
    percentage = int(x) / int(y) * 100
    if percentage > 100:
        raise ValueError
    else:
        return round(percentage)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
