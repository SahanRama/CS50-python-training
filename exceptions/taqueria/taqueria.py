import sys
menu ={
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


def main():
    total =0.00
    while True:
        item = get_item()
        if get_price(item):
            total  = total+ float(get_price(item))
            print(f"Total: ${total:.2f}")

def get_item():
    try:
        return input("Item: ").strip().title()
    except EOFError:
        print()
        sys.exit()

def get_price(item):
    if item in menu:
        return menu[item]
    else:
        return False

main()
