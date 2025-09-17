# Ternary Conditional Operator

fruits = "apple"
eat = "yes" if fruits == "apple" else "no"
print(eat)

food  = "sweet"
print("eat") if food == "sweet" else  print("don't eat")

# cleaver if condition 

age = int(input("Enter your age:"))
age  = ("Yes","No") [age<=17]
print(age)




salary =  float(input("Enter your salary:"))
tax = salary*(0.1,0.2) [salary>25000] 
print('in hand salary:',salary-tax)
print('tax:',tax)


