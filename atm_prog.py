
print("\t\t\twelcome to ATM")
balance = 10000
pin = 1234
a=int(input("enter the pin: "))
if pin == a:
    print("choose the options: ")
    print("1 - withdraw \n"
          " 2 - deposit \n"
          " 3 - change pin \n"
          " 4- balance check \n")
    x=int(input("enter the option: "))
    if x==1:
        wa = int(input("enter the amount to withdarw: "))
        w=balance-wa
        if wa>=balance:
            print("transaction invalid")
        else:
            print(f'the withdrawl amount: {wa}')
            print(f'the balance amount {w}')
    elif x==2:
        print("deposit amount")
        deposit = int(input("enter the amount to deposit: "))
        print("enter denomination")
        a = int(input("enter the count of 2000: "))
        b = int(input("enter the count of 500: "))
        c = int(input("enter the count of 200: "))
        d = int(input("enter the count of 100: "))
        count = (2000 * a) + (500 * b) + (200 * c) + (100 * d)
        if count == deposit:
            balance += count
            print(f'balance={balance}')
        else:
            print("invalid transaction")
    elif x==3:
        pa = int(input("enter the old pin: "))
        if pa == pin:
            new_pin=int(input("enter new pin: "))
            print(f'the changed pin: {new_pin}')
            pin = new_pin
            print(pin)
        else:
            print("wrong pin")
    elif x==4:
        print(f'the balance amount: {balance}')
    else:
        print("invalid option")
elif (pin!=a):
    print("\t\t\tINVALID PIN")
    print("\t\t\t RETRY AGAIN")
    
