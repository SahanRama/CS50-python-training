import inflect


def main():
    p = inflect.engine()
    names = get_names()
    say_adieu(names, p)


def get_names():
    names = []
    while True:
        try:
            name = input("Name: ")
            names.append(name)
        except EOFError:
            print()
            return names


def say_adieu(names, p):
    bye_to = p.join(names)
    print(f"Adieu, adieu, to {bye_to}")


if __name__ == "__main__":
    main()
