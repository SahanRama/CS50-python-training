def main():
    text = input("camelCase: ")
    snake_case(text)


def snake_case(word):
    for letter in word:
        if letter.islower():
            print(letter, end="")
        else:
            print(f"_{letter.lower()}", end="")
    print()


main()
