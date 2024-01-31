def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if is_start_with_two_letters(s) and is_charactor_limit_match(s) and is_starting_number_valid(s) and is_special_charactors_included(s):
        return True
    else:
        return False


def is_start_with_two_letters(word):
    # print("is_start_with_two_letters")
    return word[0:2].isalpha()

def is_charactor_limit_match(word):
    # print("is_charactor_limit_match")
    if 2 <= len(word) <=6:
       return True
    else:
       return False

def is_starting_number_valid(word):
    # print("is_starting_number_valid")
    for letter in word:
        if letter.isdigit():
            numbers= word[word.index(letter):]
            if letter == "0":
                return False
            elif word[-1:].isalpha():
                return False
            else:
                return numbers.isdigit()
    return True

def is_special_charactors_included(word):
    # print("is_special_charactors_included")
    return word.isalnum()


if __name__ == "__main__":
    main()
