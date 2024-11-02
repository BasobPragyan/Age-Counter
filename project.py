age=int(input("Enter age : "))
try:
    if (age%2==0):
        print("Your age is even")
    else:
        print("Its even")
except ValueError as ex:
    print("There is an error ",ex)
except ZeroDivisionError as ex:
    print("Exception",ex)
except SyntaxError as ex:
    print("Syntax error",ex)
except NameError as ex:
    print("Error",ex)
else:
    print("No error")
finally:
    print("Operation is complete")
    print("Your age is ",age)