# list = [1,2,3,2,1]
list = ["A","B","C","B","A"]

list_copy = list.copy()

list_copy.reverse()

if(list==list_copy):
    print("Palindrom")
else:
    print("Not Palindrom")


