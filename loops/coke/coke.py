def main():
    amount = 50
    while amount >0:
        amount = insert_coin(amount)
        print (f"Change Owed: {amount}".replace("-",""))

def insert_coin(amount):
    print(f"Amount Due: {amount}")
    coins = input("Insert Coin: ")
    if coins in ["25","10","5"]:
        amount = amount - int(coins)
    return amount


main()






