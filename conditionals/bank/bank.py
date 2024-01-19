
def main():
    answer = input("Greetings: ").strip().lower()
    greet(answer)

def greet(text):
    if text.startswith("hello"):
        print("$0")
    elif text.startswith("h"):
        print("$20")
    else :
        print("$100")

main()



