balance=0
while True:
    if balance==50 or balance>=50:
        print("YOU GOT COLA")
        balance -= 50
    else:
        print (f"Still owed <{50 - balance}> cents")

    print(f"balance is: {balance} SAR")
    print("Choose an option or write 'q' to exit:")
    try:
        Insert_Coin = input("Insert Coin: ")
        insert_coin_int = int(Insert_Coin)
        if insert_coin_int == 25:
            balance += insert_coin_int
        elif insert_coin_int == 10:
            balance += insert_coin_int
        elif insert_coin_int == 5:
            balance += insert_coin_int
        else:
            print(f"Coin not accepted. Returning {insert_coin_int} cents")
    except ValueError:
        print("Please insert a valid integer coin.")