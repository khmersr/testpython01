print("Welcome to the Pip Calculator \n")
print("============================== \n")

bill= float(input("input your TotalBill $ : "))
tip= float(input("input your Tip 10% 12% 15%  % : "))

p=int(input("how many person to pay :"))

tip_amount=bill*tip/100
total=bill+tip_amount

each_pay=total/p
print(f'Each person should pay {each_pay}$')