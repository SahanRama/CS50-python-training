import json
import sys
import requests

def main():
    # argv = get_amount()
    send_request()

def get_amount():
    if len(sys.argv) ==1:
        sys.exit("Missing command-line argument")
    elif len(sys.argv) == 2:
        try:
            return float(sys.argv[1])
        except ValueError:
            sys.exit("Command-line argument is not a number")
    else:
        sys.exit()

def send_request():
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    print(response.json())

if __name__ == "__main__":
    main()
