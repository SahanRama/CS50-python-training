import random


def main():
    level = get_level()
    score = play_game(level)
    print(f"Score :{score}")
    # print(generate_qustions(2))


def get_level():
    while True:
        try:
            level = int(input("Level :"))
            if 0 < level < 4:
                return level
            else:
                raise ValueError
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randrange(10)
    elif level ==2 :
        return random.randrange(10,100)
    else:
        return random.randrange(100,1000)


def generate_qustions(level):
    problems = []

    for _ in range(10):
        digit =[]
        x = generate_integer(level)
        y = generate_integer(level)
        digit = [x,y,x+y]
        problems.append(digit)
    return problems


def play_game(level):
    score = 0
    problems = generate_qustions(level)

    for problem in problems:
        n = 1
        x, y, answer = problem
        while n <= 3:
            n += 1
            try:
                user_answer = int(input(f"{x} + {y} = "))
                if answer == user_answer:
                    score += 1
                    break
                else:
                    raise ValueError

            except ValueError:
                print("EEE")
                pass
        if n == 4:
            print(f"{x} + {y} = {answer}")yes
    return score


if __name__ == "__main__":
    main()
