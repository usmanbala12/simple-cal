#!usr/bin/python3
print("this program calculate simple arithmetic\nenter 'add' to add\nenter 'subs' to substract\nenter 'multiply' to multiply\nenter 'divide' to divide") 
operation_type = str(input("enter the operation type"))
if operation_type == "add":
    a = float(input("enter the A value"))
    b = float(input("enter the B value"))
    answer = a+b
    print("your answer is; ", answer )
elif operation_type == "subs":
    c = float(input("enter the A value: "))
    d = float(input("enter the B value: "))
    answer1 = c-d
    print("your answer is; ", answer1)    
