dictionary = {
    'cat' : "a small animal",
    'table' : ['a piece of furniture','list of facts & figures']
}

print(dictionary)


subject = {"python","java","c++","python","javascript","python","java","c++","c"}

print(len(subject))

marks = {}

x = int(input( "Enter java marks :"))
marks.update({'java':x})

y = int(input("Enter python marks :"))
marks.update({'python':y})

z = int(input("Enter php marks :"))
marks.update({'php':z})

print(marks)