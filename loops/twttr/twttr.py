def main():
    text = input("Input: ")
    remove_vowels(text)

def remove_vowels(text):
    vowels = ["a","e","i","o","u"]
    for letter in text:
        if letter.lower() in vowels:
            print("",end="")
        else:
            print(letter, end="")
    print()

main()

