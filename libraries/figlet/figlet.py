import sys
from pyfiglet import Figlet
from random import choice

def main():
    figlet = Figlet()
    fonts = figlet.getFonts()
    validate_arguments()
    validate_fonts(fonts)
    text = get_text()
    set_fonts(figlet,fonts)
    print(figlet.renderText(text))

def get_text():
    return input("Input: ")

def validate_arguments():
    if len(sys.argv) == 2 or len(sys.argv) > 3:
        invalid_usage()
    if len(sys.argv)== 3 and sys.argv[1] not in ["-f","font"]:
        invalid_usage()

def validate_fonts(fonts):
    try :
        if sys.argv[2] not in fonts:
            invalid_usage()
    except IndexError:
        pass

def set_fonts(figlet,fonts):
    if len(sys.argv) == 1:
        figlet.setFont(font=choice(fonts))
    else:
        figlet.setFont(font = sys.argv[2])

def invalid_usage():
    sys.exit("Invalid usage")

if __name__ == "__main__":
    main()
