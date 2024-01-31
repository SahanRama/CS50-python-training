def main():
    text = input("Input: ")
    print(shorten(text))

def shorten(word):
    vowels = ["a","e","i","o","u"]
    text = ""
    for letter in word:
        if letter.lower() in vowels:
            pass
        else:
            text += letter
    return text


if __name__ == "__main__":
    main()
