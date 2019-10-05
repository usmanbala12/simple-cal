#!usr/bin/python3
print("this program calculate simple arithmetic\nenter 'add' to add\nenter 'subs' to substract\nenter 'multiply' to multiply\nenter 'divide' to divide") 
operation_type = str(input("enter the operation type: "))
while operation_type != "add" or "subs" or "multiply" or "divide":
    p = input("enter operation type again: ")
    break
    p = operation_type
if p == "add":
    a = float(input("enter the A value"))
    b = float(input("enter the B value"))
    answer = a+b
    print("your answer is; ", answer )
elif p == "subs":
    c = float(input("enter the A value: "))
    d = float(input("enter the B value: "))
    answer1 = c-d
    print("your answer is; ", answer1)  
elif p == "multiply":
    e = float(input("enter the A value: "))
    f = float(input("enter the B value: "))
    answer2 = e * f
    print("your result is equal: ", answer2)
elif p == "divide":
    g = float(input("enter the A value: "))
    h = float(input("enter the B value: "))
    answer3 = g / h
    print("your result is equal to: ", answer3)  
