import sys
import os
from PIL import Image, ImageOps

def main():
    files = get_file_names()
    create_image_with_t_shirt(files)


def get_file_names():
    name1 =os.path.splitext(sys.argv[1])
    name2 = os.path.splitext(sys.argv[2])
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments ")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif name1[1] not in [".jpg", ".jpeg", ".png"] or name2[1] not in [".jpg", ".jpeg", ".png"]:
        sys.exit("Invalid output")
    elif name1[1] != name2[1]:
        sys.exit("Input and output have different extensions")
    else:
        return sys.argv[1], sys.argv[2]

def create_image_with_t_shirt(files):
    try:
        shirt = Image.open("shirt.png")
        size = shirt.size
        input_image = Image.open(files[0])
        input_image =ImageOps.fit(input_image,size)
        input_image.paste(shirt,shirt)
        input_image.save(files[1])

    except FileNotFoundError:
        sys.exit("Input does not exist")

if __name__ == "__main__":
    main()


