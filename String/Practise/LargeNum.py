#get use three num ber then find large number

num1 = int(input("Enter Num1:"))
num2 = int(input("Enter Num2:"))
num3 = int(input("Enter Num3:"))

if(num1>num2 and num1>num3):
    print(num1)
elif( num2>num3):
    print(num2)
else:
     print(num3)
    