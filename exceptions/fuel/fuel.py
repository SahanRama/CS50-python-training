def main():
    fraction = calculate_fraction()
    if fraction <= 1 :
        print("E")
    elif fraction >= 99:
        print("F")
    else:
        print(f"{fraction}%")


def calculate_fraction():
    while True:
        try:
            text = input("Fraction: ")
            x,y =text.split("/")
            fraction = int(x)/ int(y) *100
            if fraction > 100:
                continue
            else:
                return round(fraction)
        except (ValueError, ZeroDivisionError):
            continue

main()
