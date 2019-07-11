
def calci(t,v):
     if (v>0)and (v<=9999) and (t==1):
        price=(v*3)
        print("Price for your order will be:", price)
     elif(v>9999) and (v<=50000) and (t==1):
        price=v*2.97
        print("Price is::", price)
     elif (v>50000) and (v<=100000) and (t==1):
        price=(v*2.4)
        print("Price is::", price)
     elif (v>100000) and (t==1):
        price=(v*2.1)
        print("Price is::", price)
     elif (v>0)and (v<=9999) and (t==2):
        price=v
        print("Price for your order will be:", price)
     elif (v > 9999) and (v <= 50000) and (t == 2):
         price = (v*0.99)
         print("Price is::", price)
     elif (v > 50000) and (v < 100000) and (t == 2):
         price = (v*0.8)
         print("Price is::", price)
     elif (v>100000) and (t==2):
        price=(v*0.7)
        print("Price is::", price)
     else:
         print("please input a valid input")

     repeat()

def repeat():
   try:
        print("Continue(y/n)? : ")
        choice = (input())
        if choice == 'y':
         price_calculator()
        elif choice == 'n':
         print("Thank you for checking your Price")
        else:
         print("Please Enter a Valid Input")
        price_calculator()
   except: ValueError
   print("Enter valid input")
   repeat()
def price_calculator():
    print("Price Calculator")
    type=int(input("Enter 1 for select lumber and 2 for common lumber :"))
    volume=float(input("Enter number of board feet :"))
    calci(type,volume)

price_calculator()
