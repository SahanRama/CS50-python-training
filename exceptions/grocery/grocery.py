def main():
    grocery = get_grocery()
    # print(grocery)
    display_grosery(grocery)

def get_grocery():
    groceries = {}
    try:
        while True:
            item = input().lower().strip()
            if item in groceries:
                count=int(groceries[item])
                groceries[item] = count +1
            else:
                groceries[item] = 1
            continue
    except EOFError:
        print()
        return dict(sorted(groceries.items()))

def display_grosery(list):
    for item in list:
        print(f"{list[item]} {item.upper()}")

if __name__ == "__main__":
    main()
