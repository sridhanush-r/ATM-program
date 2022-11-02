
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


'''

print("calculator")
a=int(input("enter the 1st value:"))
s=int(input("enter the 2nd value:"))
x=int(input("1.add"
      "\n2.subract"
      "\n3.multiply"
      "\n4. divde"
      "\nenter the choice:"))
if x==1 :
      print(f'add value: {a+s} ')
elif x==2 :
      print(f'subract value: {a-s} ')
elif x==3 :
      print(f'multiply value: {a*s} ')
elif x== 4:
      print(f'divide value: {a/s} ')
else:
    print("wrong operation")





n=int(input("enter n:"))
for i in range(n,-1,-1):
      print(i)

num=int(input("ent num:"))
c=0
if num==0 or num==-1:
      print("count:1")
else:
      while num!=0 and num!=-1:
            num=num // 10
            c+=1
      print("count:",c)







n=int(input("enter a number:"))
s=0
while n>0:
    add=n%10
    s+=add
    n=n//10
print("sum:",s)






n=int(input("num="))
mult=1
while n>0:
    s = n%10
    mult*=s
    n=n//10
print("multiply:",mult)






n=int(input("enter n:"))
rev=0
while n!=0:
    r=n%10
    rev = rev*10+r
    n//=10
print("revrse:" ,rev)





o=[]
u=int(input("number:"))
count=0
for i in range(2,u):
    if (u%i)==0:
        print(f"{u} not prime")
        break
    else:
        print(f"{u} prime")
'''