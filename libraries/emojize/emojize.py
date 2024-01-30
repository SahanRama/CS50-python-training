import emoji

def main():
    text = input("Input: ").strip()
    print(emoji.emojize(f"Output: {text}", language ="alias"))

if __name__ == "__main__":
    main()
