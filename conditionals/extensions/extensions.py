def main():
    answer  = input("File name: ").strip().lower()
    media_type(answer)


def media_type(name):
    if name.endswith(".gif"):
        print("image/gif")
    elif name.endswith(".jpeg") or name.endswith("jpg"):
        print("image/jpeg")
    elif name.endswith(".png"):
        print("image/png")
    elif name.endswith(".pdf"):
        print("application/pdf")
    elif name.endswith(".txt"):
        print("text/plain")
    elif name.endswith(".zip"):
        print("application/zip")
    else:
        print("application/octet-stream")


main()
