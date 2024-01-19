def main():
    time = input("What time is it? ")
    c_time = convert(time)
    if 18.00 <= c_time <= 19.00:
        print("dinner time")
    elif 12.00 <= c_time <= 13.00:
        print("lunch time")
    elif 7.00 <= c_time <= 8.00:
        print("breakfast time")

def convert(time):
    hours, mins = time.split(":")
    converted_time = int(hours)+ int(mins)/60
    return round(converted_time,2)


if __name__ == "__main__":
    main()
