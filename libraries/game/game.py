from random import randint
import sys


def main():
    level = get_level()
    guess_number(level)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                return level
        except ValueError:
            pass


def guess_number(level):
    rndm_number = randint(1, level)
    while True:
        try:
            user_number = int(input("Guess: "))

            if user_number == rndm_number:
                sys.exit("Just right!")
            elif user_number > rndm_number:
                print("Too large!")
            else:
                print("Too small!")

        except ValueError:
            pass


if __name__ == "__main__":
    main()
