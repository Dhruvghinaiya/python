age = int(input("Enter your age: "))

if age>=18 and age<19:
    print("You are eligible to vote.")
elif  age>=19 and age<25:
    print("You are eligible for voting and you are young.")
elif  age>=26 and age<60:
    print("You are eligible for voting and you are adult.")
elif age>=60 :
    print("You are eligible for voting and you are senior citizen.") 
else: 
    print("You are not eligible to vote.")